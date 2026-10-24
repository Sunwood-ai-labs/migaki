from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_repo import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        (self.root / "SKILL.md").write_text(
            "---\nname: sample-skill\ndescription: A test skill\n---\n"
            "See [evidence](references/evidence.md).\n",
            encoding="utf-8",
        )
        (self.root / "LICENSE").write_text("MIT test license\n", encoding="utf-8")
        (self.root / "NOTICE.md").write_text("Attribution notice\n", encoding="utf-8")
        (self.root / "agents").mkdir()
        (self.root / "agents" / "openai.yaml").write_text(
            "interface:\n"
            "  display_name: Sample\n"
            "  short_description: A sample skill\n"
            "  default_prompt: Use the sample skill.\n",
            encoding="utf-8",
        )
        (self.root / "references").mkdir()
        (self.root / "references" / "evidence.md").write_text("Evidence.\n", encoding="utf-8")

    def test_valid_repository_passes(self) -> None:
        self.assertEqual(validate_repository(self.root), [])

    def test_missing_relative_reference_is_reported(self) -> None:
        (self.root / "SKILL.md").write_text(
            "---\nname: sample-skill\ndescription: A test skill\n---\n"
            "See [missing](references/not-here.md).\n",
            encoding="utf-8",
        )

        issues = validate_repository(self.root)

        self.assertTrue(any("relative link target does not exist" in issue.message for issue in issues))

    def test_code_examples_and_anchors_do_not_create_false_link_failures(self) -> None:
        (self.root / "SKILL.md").write_text(
            "---\nname: sample-skill\ndescription: A test skill\n---\n"
            "[same page](#details)\n\n"
            "```markdown\n[not a real link](references/not-here.md)\n```\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(self.root), [])

    def test_existing_directory_link_is_valid(self) -> None:
        (self.root / "README.md").write_text("[references](references/)\n", encoding="utf-8")

        self.assertEqual(validate_repository(self.root), [])

    def test_markdown_document_asset_link_is_checked(self) -> None:
        docs = self.root / "docs"
        assets = docs / "assets"
        assets.mkdir(parents=True)
        (assets / "logo.svg").write_text("<svg/>\n", encoding="utf-8")
        page = docs / "index.md"
        page.write_text("![logo](assets/logo.svg)\n", encoding="utf-8")

        self.assertEqual(validate_repository(self.root), [])

        page.write_text("![missing logo](assets/missing.svg)\n", encoding="utf-8")
        issues = validate_repository(self.root)
        self.assertTrue(any("docs/index.md" == issue.path for issue in issues))
        self.assertTrue(any("assets/missing.svg" in issue.message for issue in issues))

    def test_placeholder_marker_in_prose_is_reported_but_example_is_ignored(self) -> None:
        (self.root / "README.md").write_text(
            "TODO: replace this before release.\n\n"
            "```text\nTODO: this is an example.\n```\n",
            encoding="utf-8",
        )

        issues = validate_repository(self.root)

        self.assertEqual(sum("unresolved placeholder" in issue.message for issue in issues), 1)

    def test_absolute_user_path_and_secret_assignment_are_reported(self) -> None:
        readme = self.root / "README.md"
        local_path = "C:" + chr(92) + "Users" + chr(92) + "sample" + chr(92) + "notes.md"
        secret = "A" * 24
        readme.write_text(f"Path: {local_path}\n`api_key={secret}`\n", encoding="utf-8")

        issues = validate_repository(self.root)

        messages = [issue.message for issue in issues]
        self.assertIn("absolute local user path found", messages)
        self.assertIn("possible credential value assigned to a secret field", messages)


if __name__ == "__main__":
    unittest.main()
