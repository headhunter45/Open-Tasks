"""Tests for repository scanner and WorkItem index."""

import unittest
from pathlib import Path

from ot.scanner import RepositoryScanner, WorkItemIndex, load_index


class TestScannerAndIndex(unittest.TestCase):
    def setUp(self):
        self.sample_root = Path(__file__).resolve().parent.parent / "examples" / "sample-project"

    def test_repository_scanner_finds_all_items(self):
        scanner = RepositoryScanner(self.sample_root)
        items = scanner.scan_tasks_directory()
        self.assertEqual(len(items), 4)

        titles = {item.title for item in items}
        self.assertIn("Release Alpha", titles)
        self.assertIn("Implement User Authentication", titles)
        self.assertIn("Fix Login Crash on Null Password", titles)
        self.assertIn("Setup Continuous Integration Pipeline", titles)

    def test_work_item_index_hierarchy_and_dependencies(self):
        idx = load_index(self.sample_root)

        # Lookup by title
        alpha = idx.resolve("Release Alpha")
        self.assertEqual(alpha.type, "epic")

        # Lookup by short ID prefix
        short_id = idx.get_short_id(alpha.id)
        resolved_alpha = idx.resolve(short_id)
        self.assertEqual(resolved_alpha.id, alpha.id)

        # Children
        children = idx.get_children(alpha.id)
        self.assertEqual(len(children), 1)
        self.assertEqual(children[0].title, "Implement User Authentication")

        # Parent
        auth_item = idx.resolve("Implement User Authentication")
        parent = idx.get_parent(auth_item)
        self.assertIsNotNone(parent)
        self.assertEqual(parent.id, alpha.id)

        # Dependencies
        bug_item = idx.resolve("Fix Login Crash on Null Password")
        deps = idx.get_dependencies(bug_item)
        self.assertEqual(len(deps), 1)
        self.assertEqual(deps[0].id, auth_item.id)

        # Dependents (blocked by)
        dependents = idx.get_dependents(auth_item)
        self.assertEqual(len(dependents), 1)
        self.assertEqual(dependents[0].id, bug_item.id)

    def test_filtering(self):
        idx = load_index(self.sample_root)
        bugs = idx.filter(item_type="bug")
        self.assertEqual(len(bugs), 1)
        self.assertEqual(bugs[0].title, "Fix Login Crash on Null Password")

        in_prog = idx.filter(status="in_progress")
        self.assertEqual(len(in_prog), 2)


if __name__ == "__main__":
    unittest.main()
