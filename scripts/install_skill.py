#!/usr/bin/env python3
"""Install this repository's Agent Skill bundle without overwriting user files."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
BUNDLE_FILES = ("SKILL.md", "LICENSE", "NOTICE.md")
BUNDLE_DIRECTORIES = ("agents", "references")
REPARSE_POINT_ATTRIBUTE = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


class InstallError(Exception):
    """A safe installation could not be completed."""


@dataclass(frozen=True)
class InstallResult:
    destination: Path
    installed: bool


def _is_link_or_reparse_point(path: Path) -> bool:
    try:
        details = path.lstat()
    except FileNotFoundError:
        return False
    return path.is_symlink() or bool(
        getattr(details, "st_file_attributes", 0) & REPARSE_POINT_ATTRIBUTE
    )


def _check_path_components(path: Path) -> Path:
    """Return an absolute path after rejecting links in every existing component."""
    expanded = Path(os.path.expanduser(os.fspath(path)))
    if not expanded.is_absolute():
        expanded = Path.cwd() / expanded

    current = Path(expanded.anchor)
    for component in expanded.parts[1:]:
        if component in ("", "."):
            continue
        if component == "..":
            current = current.parent
            continue
        current /= component
        if _is_link_or_reparse_point(current):
            raise InstallError(f"refusing a symbolic link or reparse point in path: {current}")
    return current


def _bundle_entries(source_root: Path) -> tuple[dict[Path, Path], set[Path]]:
    files: dict[Path, Path] = {}
    directories: set[Path] = set()

    for filename in BUNDLE_FILES:
        source = source_root / filename
        if _is_link_or_reparse_point(source) or not source.is_file():
            raise InstallError(f"required regular file is missing: {source}")
        files[Path(filename)] = source

    for dirname in BUNDLE_DIRECTORIES:
        source_dir = source_root / dirname
        if _is_link_or_reparse_point(source_dir) or not source_dir.is_dir():
            raise InstallError(f"required regular directory is missing: {source_dir}")
        directories.add(Path(dirname))

        for current_root, dirnames, filenames in os.walk(source_dir, followlinks=False):
            current = Path(current_root)
            relative_dir = current.relative_to(source_root)
            for name in list(dirnames):
                child = current / name
                if _is_link_or_reparse_point(child):
                    raise InstallError(f"refusing a symbolic link or reparse point in bundle: {child}")
                directories.add(child.relative_to(source_root))
            for name in filenames:
                child = current / name
                if _is_link_or_reparse_point(child) or not child.is_file():
                    raise InstallError(f"refusing a non-regular bundle file: {child}")
                files[child.relative_to(source_root)] = child

    return files, directories


def _destination_entries(destination: Path) -> tuple[dict[Path, Path], set[Path]]:
    if _is_link_or_reparse_point(destination):
        raise InstallError(f"refusing a symbolic link or reparse point at destination: {destination}")
    if not destination.is_dir():
        raise InstallError(f"destination exists and is not a directory: {destination}")

    files: dict[Path, Path] = {}
    directories: set[Path] = set()
    for current_root, dirnames, filenames in os.walk(destination, followlinks=False):
        current = Path(current_root)
        for name in list(dirnames):
            child = current / name
            if _is_link_or_reparse_point(child):
                raise InstallError(f"refusing a symbolic link or reparse point in existing bundle: {child}")
            directories.add(child.relative_to(destination))
        for name in filenames:
            child = current / name
            if _is_link_or_reparse_point(child) or not child.is_file():
                raise InstallError(f"refusing a non-regular file in existing bundle: {child}")
            files[child.relative_to(destination)] = child
    return files, directories


def _is_identical(
    source_files: dict[Path, Path],
    source_directories: set[Path],
    destination: Path,
) -> bool:
    destination_files, destination_directories = _destination_entries(destination)
    if source_directories != destination_directories or source_files.keys() != destination_files.keys():
        return False
    return all(
        source_files[relative].read_bytes() == destination_files[relative].read_bytes()
        for relative in source_files
    )


def _skill_name(source_root: Path) -> str:
    """Use the skill's frontmatter name as the child directory name."""
    text = (source_root / "SKILL.md").read_text(encoding="utf-8")
    first_line, separator, remaining = text.partition("\n")
    if first_line.strip() != "---" or not separator:
        raise InstallError("SKILL.md must start with YAML frontmatter")
    frontmatter, closing, _ = remaining.partition("\n---")
    if not closing:
        raise InstallError("SKILL.md has no closing YAML frontmatter delimiter")
    for line in frontmatter.splitlines():
        key, colon, value = line.partition(":")
        if colon and key.strip() == "name":
            name = value.strip().strip("\"'")
            if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                return name
    raise InstallError("SKILL.md frontmatter must contain a lowercase skill name")


def install_skill(
    skills_parent: Path,
    source_root: Path = REPOSITORY_ROOT,
) -> InstallResult:
    source_root = _check_path_components(source_root)
    skills_parent = _check_path_components(skills_parent)
    source_files, source_directories = _bundle_entries(source_root)
    name = _skill_name(source_root)

    try:
        skills_parent.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        raise InstallError(f"cannot create skills directory {skills_parent}: {error}") from error
    skills_parent = _check_path_components(skills_parent)
    if not skills_parent.is_dir():
        raise InstallError(f"skills destination is not a directory: {skills_parent}")

    destination = skills_parent / name
    if _is_link_or_reparse_point(destination):
        raise InstallError(f"refusing a symbolic link or reparse point at destination: {destination}")
    if destination.exists():
        if _is_identical(source_files, source_directories, destination):
            return InstallResult(destination=destination, installed=False)
        raise InstallError(f"destination already exists with different contents; left untouched: {destination}")

    try:
        with tempfile.TemporaryDirectory(prefix=f".{name}.install-", dir=skills_parent) as staging_name:
            staging = Path(staging_name) / name
            staging.mkdir()
            for relative in sorted(source_directories, key=lambda entry: (len(entry.parts), str(entry))):
                (staging / relative).mkdir(exist_ok=True)
            for relative, source in sorted(source_files.items(), key=lambda item: str(item[0])):
                target = staging / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            os.rename(staging, destination)
    except FileExistsError as error:
        raise InstallError(f"destination appeared during installation; left untouched: {destination}") from error
    except OSError as error:
        raise InstallError(f"installation failed before completion: {error}") from error

    return InstallResult(destination=destination, installed=True)


def _arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        metavar="SKILLS_PARENT",
        help="skills parent directory (default: ~/.codex/skills)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = _arguments(argv)
    try:
        result = install_skill(arguments.destination)
    except (InstallError, OSError, UnicodeError) as error:
        print(f"Install failed: {error}", file=sys.stderr)
        return 1

    action = "Installed" if result.installed else "Already up to date"
    print(f"{action}: {result.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
