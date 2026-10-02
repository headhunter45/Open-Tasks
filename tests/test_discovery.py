"""Tests for project and VCS discovery."""

import os
import tempfile
import unittest
from pathlib import Path

from ot.discovery import find_project_root, find_vcs_root, discover_root


class TestProjectDiscovery(unittest.TestCase):
    def test_find_project_root_in_nested_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir).resolve()
            ot_dir = root / ".ot"
            ot_dir.mkdir()
            nested = root / "src" / "deeply" / "nested" / "folder"
            nested.mkdir(parents=True)

            found = find_project_root(nested)
            self.assertEqual(found, root)

    def test_find_project_root_from_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir).resolve()
            (root / ".ot").mkdir()
            test_file = root / "subdir" / "file.txt"
            test_file.parent.mkdir()
            test_file.touch()

            found = find_project_root(test_file)
            self.assertEqual(found, root)

    def test_find_project_root_not_found(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir).resolve()
            found = find_project_root(root)
            self.assertIsNone(found)

    def test_environment_variable_override(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir).resolve()
            (root / ".ot").mkdir()
            other = root / "other"
            other.mkdir()

            old_env = os.environ.get("OPEN_TASKS_ROOT")
            try:
                os.environ["OPEN_TASKS_ROOT"] = str(root)
                found = find_project_root(other)
                self.assertEqual(found, root)
            finally:
                if old_env is not None:
                    os.environ["OPEN_TASKS_ROOT"] = old_env
                else:
                    os.environ.pop("OPEN_TASKS_ROOT", None)


if __name__ == "__main__":
    unittest.main()
