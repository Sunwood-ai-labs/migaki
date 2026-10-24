#!/usr/bin/env python3
"""Validate public repository metadata, documentation links, and source hygiene."""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRECTORIES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
}
TEXT_SUFFIXES = {
    ".cff",
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".py",
    ".sh",
    ".svg",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".vue",
    ".yaml",
    ".yml",
}
INLINE_LINK = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(?:<(?P<angle>[^>]+)>|(?P<plain>[^)\s]+))"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
REFERENCE_DEFINITION = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))", re.MULTILINE)
FENCE_START = re.compile(r"^ {0,3}(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(?P<ticks>`+).*?(?P=ticks)(?!`)", re.DOTALL)
URL_TEXT = re.compile(r"(?i)\b(?:https?|ftp)://[^\s<>]+")
WINDOWS_USER_PATH = re.compile(r"(?i)\b[A-Z]:[\\/]+Users[\\/]+[^\\/\s`\"')]+(?:[\\/][^\\/\s`\"')]+)*")
POSIX_USER_PATH = re.compile(r"(?<![A-Za-z0-9:])/(?:Users|home)/[^/\s`\"')]+(?:/[^/\s`\"')]+)*")
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")
GITHUB_TOKEN = re.compile(r"gh(?:p|o|u|r|s)_[A-Za-z0-9]{36,}")
GITHUB_FINE_GRAINED_TOKEN = re.compile(r"github_pat_[A-Za-z0-9_]{50,}")
AWS_ACCESS_KEY = re.compile(r"\bAKIA[0-9A-Z]{16}\b")
GOOGLE_API_KEY = re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")
OPENAI_SECRET = re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b")
SLACK_TOKEN = re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")
STRIPE_SECRET = re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{20,}\b")
JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\b")
SECRET_ASSIGNMENT = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|secret)"
    r"\s*[:=]\s*[\"']?([A-Za-z0-9][A-Za-z0-9_./+=-]{19,})"
)
PLACEHOLDER_LINE = re.compile(r"(?i)^\s*(?:[-*+]\s*)?(?:TODO|FIXME|TBD|CHANGEME)\b(?:\s*[:(]|$)")
PLACEHOLDER_NAME = re.compile(
    r"(?i)\b(?:your[-_](?:username|owner|repo|token|api[-_]key)"
    r"|replace[-_]with[-_]your[-_]value|insert[-_]your[-_]value)\b"
)
PLACEHOLDER_SECRET_VALUE = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|secret)"
    r"\s*[:=]\s*[\"']?(?:your[-_]|replace[-_]|insert[-_]|placeholder\b|changeme\b|<your)"
)
SECRET_PATTERNS = (
    ("private key block", PRIVATE_KEY),
    ("GitHub token", GITHUB_TOKEN),
    ("GitHub fine-grained token", GITHUB_FINE_GRAINED_TOKEN),
    ("AWS access key", AWS_ACCESS_KEY),
    ("Google API key", GOOGLE_API_KEY),
    ("OpenAI secret key", OPENAI_SECRET),
    ("Slack token", SLACK_TOKEN),
    ("Stripe secret key", STRIPE_SECRET),
    ("JWT", JWT),
)


@dataclass(frozen=True)
class Issue:
    path: str
    message: str
    line: int | None = None

    def __str__(self) -> str:
        location = f"{self.path}:{self.line}" if self.line is not None else self.path
        return f"{location}: {self.message}"


def _relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _read_utf8(path: Path, root: Path, issues: list[Issue]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        issues.append(Issue(_relative_path(path, root), "text file is not valid UTF-8"))
    except OSError as error:
        issues.append(Issue(_relative_path(path, root), f"cannot read file: {error}"))
    return None


def _yaml_mapping(text: str, path: str, issues: list[Issue]) -> dict[str, object] | None:
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as error:
        mark = getattr(error, "problem_mark", None)
        line = mark.line + 1 if mark is not None else None
        issues.append(Issue(path, "invalid YAML", line))
        return None
    if not isinstance(data, dict):
        issues.append(Issue(path, "expected a YAML mapping"))
        return None
    return data


def _validate_skill_frontmatter(root: Path, issues: list[Issue]) -> None:
    path = root / "SKILL.md"
    if not path.is_file():
        issues.append(Issue("SKILL.md", "required skill file is missing"))
        return
    text = _read_utf8(path, root, issues)
    if text is None:
        return
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        issues.append(Issue("SKILL.md", "must start with YAML frontmatter", 1))
        return
    try:
        closing = lines.index("---", 1)
    except ValueError:
        issues.append(Issue("SKILL.md", "has no closing YAML frontmatter delimiter"))
        return
    metadata = _yaml_mapping("\n".join(lines[1:closing]), "SKILL.md", issues)
    if metadata is None:
        return
    for key in ("name", "description"):
        value = metadata.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(Issue("SKILL.md", f"frontmatter field {key!r} must be a non-empty string"))
    name = metadata.get("name")
    if isinstance(name, str) and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        issues.append(Issue("SKILL.md", "frontmatter name must be a lowercase hyphenated slug"))


def _validate_agent_manifest(root: Path, issues: list[Issue]) -> None:
    relative = "agents/openai.yaml"
    path = root / relative
    if not path.is_file():
        issues.append(Issue(relative, "required agent manifest is missing"))
        return
    text = _read_utf8(path, root, issues)
    if text is None:
        return
    manifest = _yaml_mapping(text, relative, issues)
    if manifest is None:
        return
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        issues.append(Issue(relative, "must define an interface mapping"))
        return
    for key in ("display_name", "short_description", "default_prompt"):
        value = interface.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(Issue(relative, f"interface field {key!r} must be a non-empty string"))


def _mask_fenced_code(text: str) -> str:
    output: list[str] = []
    fence_character: str | None = None
    fence_length = 0
    for line in text.splitlines(keepends=True):
        match = FENCE_START.match(line)
        if fence_character is None:
            if match is not None:
                fence_character = match.group(1)[0]
                fence_length = len(match.group(1))
                output.append("\n" if line.endswith("\n") else "")
            else:
                output.append(line)
            continue

        closing = re.match(rf"^ {{0,3}}{re.escape(fence_character)}{{{fence_length},}}[ \t]*(?:\r?\n)?$", line)
        output.append("\n" if line.endswith("\n") else "")
        if closing:
            fence_character = None
            fence_length = 0
    return "".join(output)


def _mask_inline_code(text: str) -> str:
    return INLINE_CODE.sub(lambda match: "\n" * match.group(0).count("\n"), text)


def _markdown_targets(text: str) -> list[tuple[str, int]]:
    prose = _mask_inline_code(_mask_fenced_code(text))
    targets: list[tuple[str, int]] = []
    for pattern in (INLINE_LINK, REFERENCE_DEFINITION):
        for match in pattern.finditer(prose):
            target = match.group("angle") if "angle" in match.groupdict() else match.group(1)
            if target is None:
                target = match.group("plain") if "plain" in match.groupdict() else match.group(2)
            if target:
                targets.append((target.strip(), prose.count("\n", 0, match.start()) + 1))
    return targets


def _local_link_candidates(root: Path, source: Path, path_text: str) -> list[Path]:
    decoded = unquote(path_text)
    if decoded.startswith("/"):
        docs_root = root / "docs"
        relative = PurePosixPath(decoded.lstrip("/"))
        base = docs_root.joinpath(*relative.parts)
        public = docs_root / "public" / Path(*relative.parts)
    else:
        relative = PurePosixPath(decoded.replace("\\", "/"))
        base = source.parent.joinpath(*relative.parts)
        public = base

    candidates = [base]
    if not relative.suffix:
        candidates.extend((base.with_suffix(".md"), base / "index.md", base / "index.html"))
    if decoded.startswith("/"):
        candidates.append(public)
        if not relative.suffix:
            candidates.extend((public.with_suffix(".md"), public / "index.md", public / "index.html"))
    return candidates


def _validate_markdown_links(root: Path, files: list[Path], issues: list[Issue]) -> None:
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = _read_utf8(path, root, issues)
        if text is None:
            continue
        relative = _relative_path(path, root)
        for target, line in _markdown_targets(text):
            if not target or target.startswith("#") or target.startswith("//"):
                continue
            parsed = urlsplit(target)
            if parsed.scheme:
                continue
            if not parsed.path:
                continue
            candidates = _local_link_candidates(root, path, parsed.path)
            valid = False
            for candidate in candidates:
                try:
                    resolved = candidate.resolve(strict=False)
                    resolved.relative_to(root)
                except (OSError, ValueError):
                    continue
                if resolved.is_file() or resolved.is_dir():
                    valid = True
                    break
            if not valid:
                issues.append(Issue(relative, f"relative link target does not exist: {target}", line))


def _source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for current_root, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(current_root)
        dirnames[:] = sorted(
            name for name in dirnames if name not in IGNORED_DIRECTORIES and not (current / name).is_symlink()
        )
        for name in sorted(filenames):
            path = current / name
            if path.suffix.lower() in TEXT_SUFFIXES or not path.suffix:
                files.append(path)
    return files


def _strip_markdown_examples(text: str) -> str:
    text = _mask_inline_code(_mask_fenced_code(text))
    return URL_TEXT.sub("", text)


def _validate_source_hygiene(root: Path, files: list[Path], issues: list[Issue]) -> None:
    for path in files:
        try:
            content = path.read_bytes()
        except OSError as error:
            issues.append(Issue(_relative_path(path, root), f"cannot read file: {error}"))
            continue
        if b"\0" in content:
            continue
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            issues.append(Issue(_relative_path(path, root), "text file is not valid UTF-8"))
            continue

        relative = _relative_path(path, root)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    issues.append(Issue(relative, f"possible {label} detected", line_number))
            if SECRET_ASSIGNMENT.search(line):
                issues.append(Issue(relative, "possible credential value assigned to a secret field", line_number))
            if WINDOWS_USER_PATH.search(line) or POSIX_USER_PATH.search(line):
                issues.append(Issue(relative, "absolute local user path found", line_number))

        marker_text = _strip_markdown_examples(text) if path.suffix.lower() == ".md" else text
        for line_number, line in enumerate(marker_text.splitlines(), start=1):
            if PLACEHOLDER_LINE.search(line) or PLACEHOLDER_NAME.search(line) or PLACEHOLDER_SECRET_VALUE.search(line):
                issues.append(Issue(relative, "unresolved placeholder found", line_number))


def validate_repository(root: Path = REPOSITORY_ROOT) -> list[Issue]:
    root = root.resolve()
    issues: list[Issue] = []
    if not root.is_dir():
        return [Issue(".", "repository root is not a directory")]

    for required in ("LICENSE", "NOTICE.md"):
        if not (root / required).is_file():
            issues.append(Issue(required, "required public distribution file is missing"))
    if not (root / "references").is_dir():
        issues.append(Issue("references", "required references directory is missing"))

    _validate_skill_frontmatter(root, issues)
    _validate_agent_manifest(root, issues)
    files = _source_files(root)
    _validate_markdown_links(root, files, issues)
    _validate_source_hygiene(root, files, issues)
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT, help="repository root to validate")
    arguments = parser.parse_args(argv)

    issues = validate_repository(arguments.root)
    if issues:
        for issue in issues:
            print(f"ERROR {issue}", file=sys.stderr)
        print(f"Validation failed with {len(issues)} issue(s).", file=sys.stderr)
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
