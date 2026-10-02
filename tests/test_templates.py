"""Tests for template generation, installation, and retrieval."""

import tempfile
import unittest
from pathlib import Path

from ot.templates import DEFAULT_TEMPLATES, get_template, install_default_templates


class TestTemplates(unittest.TestCase):
    def test_default_templates_collection(self):
        self.assertIn("tasks/default.md", DEFAULT_TEMPLATES)
        self.assertIn("tasks/bug.md", DEFAULT_TEMPLATES)
        self.assertIn("tasks/feature.md", DEFAULT_TEMPLATES)
        self.assertIn("tasks/epic.md", DEFAULT_TEMPLATES)
        self.assertIn("tasks/chore.md", DEFAULT_TEMPLATES)
        self.assertIn("tasks/spike.md", DEFAULT_TEMPLATES)
        self.assertIn("meetings/grooming.md", DEFAULT_TEMPLATES)
        self.assertIn("meetings/planning.md", DEFAULT_TEMPLATES)
        self.assertIn("meetings/retrospective.md", DEFAULT_TEMPLATES)
        self.assertIn("meetings/ideation.md", DEFAULT_TEMPLATES)
        self.assertIn("shared/comment.md", DEFAULT_TEMPLATES)

    def test_install_default_templates(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / ".ot").mkdir()

            installed = install_default_templates(root)
            self.assertEqual(installed, len(DEFAULT_TEMPLATES))

            # Calling again without overwrite should install 0
            reinstalled = install_default_templates(root)
            self.assertEqual(reinstalled, 0)

            # Retrieve local template
            bug_tmpl = get_template("tasks/bug.md", root)
            self.assertIsNotNone(bug_tmpl)
            self.assertIn("Steps to Reproduce", bug_tmpl)


if __name__ == "__main__":
    unittest.main()
