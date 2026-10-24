from __future__ import annotations

import os
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import scripts.install_skill as installer_module
from scripts.install_skill import InstallError, install_skill


class InstallSkillTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "SKILL.md").write_text(
            "---\nname: sample-skill\ndescription: A test skill\n---\n"
            "See [evidence](references/evidence.md).\n",
            encoding="utf-8",
        )
        (self.source / "LICENSE").write_text("MIT test license\n", encoding="utf-8")
        (self.source / "NOTICE.md").write_text("Attribution notice\n", encoding="utf-8")
        (self.source / "agents").mkdir()
        (self.source / "agents" / "openai.yaml").write_text("interface: {}\n", encoding="utf-8")
        (self.source / "references").mkdir()
        (self.source / "references" / "evidence.md").write_text("Evidence.\n", encoding="utf-8")
        (self.source / "README.md").write_text("This is not part of the installed bundle.\n", encoding="utf-8")
        (self.source / "docs").mkdir()
        (self.source / "docs" / "guide.md").write_text("Docs are not part of the installed bundle.\n", encoding="utf-8")
        self.destination = self.root / "skills"

    def test_installs_only_the_skill_and_license_bundle(self) -> None:
        result = install_skill(self.destination, self.source)

        self.assertTrue(result.installed)
        self.assertEqual(result.destination, self.destination / "sample-skill")
        installed_files = {
            path.relative_to(result.destination).as_posix()
            for path in result.destination.rglob("*")
            if path.is_file()
        }
        self.assertEqual(
            installed_files,
            {
                "LICENSE",
                "NOTICE.md",
                "SKILL.md",
                "agents/openai.yaml",
                "references/evidence.md",
            },
        )

    def test_identical_install_is_a_no_op(self) -> None:
        first = install_skill(self.destination, self.source)
        installed_file = first.destination / "SKILL.md"
        original_mtime = installed_file.stat().st_mtime_ns

        second = install_skill(self.destination, self.source)

        self.assertTrue(first.installed)
        self.assertFalse(second.installed)
        self.assertEqual(installed_file.stat().st_mtime_ns, original_mtime)

    def test_conflicting_destination_is_preserved(self) -> None:
        target = self.destination / "sample-skill"
        target.mkdir(parents=True)
        existing = target / "SKILL.md"
        existing.write_text("User-owned content.\n", encoding="utf-8")
        sentinel = target / "keep.txt"
        sentinel.write_text("Keep this file.\n", encoding="utf-8")

        with self.assertRaisesRegex(InstallError, "left untouched"):
            install_skill(self.destination, self.source)

        self.assertEqual(existing.read_text(encoding="utf-8"), "User-owned content.\n")
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "Keep this file.\n")

    def test_failed_copy_leaves_no_partial_install(self) -> None:
        copy_file = installer_module.shutil.copyfile
        calls = 0

        def fail_after_one_file(source: Path, destination: Path) -> Path:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated copy failure")
            return copy_file(source, destination)

        with patch("scripts.install_skill.shutil.copyfile", side_effect=fail_after_one_file):
            with self.assertRaisesRegex(InstallError, "installation failed before completion"):
                install_skill(self.destination, self.source)

        self.assertFalse((self.destination / "sample-skill").exists())
        self.assertEqual(list(self.destination.glob(".sample-skill.install-*")), [])

    def test_refuses_source_symlinks_when_platform_allows_them(self) -> None:
        outside = self.root / "outside.md"
        outside.write_text("outside the bundle\n", encoding="utf-8")
        link = self.source / "references" / "outside.md"
        try:
            os.symlink(outside, link)
        except (NotImplementedError, OSError, PermissionError) as error:
            self.skipTest(f"symlink creation unavailable: {error}")

        with self.assertRaisesRegex(InstallError, "symbolic link"):
            install_skill(self.destination, self.source)
        self.assertFalse((self.destination / "sample-skill").exists())

    def test_refuses_symlinked_skills_parent_when_platform_allows_them(self) -> None:
        actual_parent = self.root / "actual-skills"
        actual_parent.mkdir()
        linked_parent = self.root / "linked-skills"
        try:
            os.symlink(actual_parent, linked_parent, target_is_directory=True)
        except (NotImplementedError, OSError, PermissionError) as error:
            self.skipTest(f"symlink creation unavailable: {error}")

        with self.assertRaisesRegex(InstallError, "symbolic link"):
            install_skill(linked_parent, self.source)
        self.assertEqual(list(actual_parent.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
