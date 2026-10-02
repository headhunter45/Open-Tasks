"""Tests for validation, error reporting, and repair framework."""

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ot.cli import main
from ot.validation import Diagnostic, Repairer, Severity, Validator


class TestValidationAndRepair(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.root = Path(self.tmpdir)
        sample_src = Path(__file__).resolve().parent.parent / "examples" / "sample-project"
        shutil.copytree(sample_src, self.root, dirs_exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_sample_project_clean_validation(self):
        # Create templates & meetings dirs so project is fully clean
        (self.root / ".ot" / "templates").mkdir(exist_ok=True)
        (self.root / ".ot" / "meetings").mkdir(exist_ok=True)

        validator = Validator(self.root)
        diags = validator.validate_all()
        errors = [d for d in diags if d.severity == Severity.ERROR]
        self.assertEqual(len(errors), 0)

    def test_missing_directory_detection_and_repair(self):
        # Remove templates and meetings if present
        shutil.rmtree(self.root / ".ot" / "templates", ignore_errors=True)
        shutil.rmtree(self.root / ".ot" / "meetings", ignore_errors=True)

        validator = Validator(self.root)
        diags = validator.validate_all()
        missing_dirs = [d for d in diags if d.category == "filesystem" and d.is_fixable]
        self.assertGreaterEqual(len(missing_dirs), 1)

        # Repair missing directories
        repairer = Repairer(self.root)
        repairs = repairer.repair()
        self.assertTrue(any("templates" in r for r in repairs))
        self.assertTrue((self.root / ".ot" / "templates").is_dir())


    def test_protected_key_misplacement_detection_and_repair(self):
        # Put protected key in config.local.json
        local_cfg = self.root / ".ot" / "config.local.json"
        local_cfg.write_text(
            json.dumps({"workItem": {"types": {"custom": {"label": "Custom"}}}}),
            encoding="utf-8",
        )

        validator = Validator(self.root)
        diags = validator.validate_all()
        warnings = [d for d in diags if d.category == "config" and d.is_fixable]
        self.assertGreaterEqual(len(warnings), 1)

        # Run repair
        repairer = Repairer(self.root)
        repairs = repairer.repair()
        self.assertTrue(any("config.local.json" in r for r in repairs))

        # Check that protected key was moved to config.json
        proj_cfg_data = json.loads((self.root / ".ot" / "config.json").read_text(encoding="utf-8"))
        self.assertIn("workItem", proj_cfg_data)

    def test_self_dependency_detection_and_repair(self):
        # Add self-dependency to an item
        task_file = self.root / ".ot" / "tasks" / "FixLoginCrash" / "index.md"
        content = task_file.read_text(encoding="utf-8")
        # Add self-UUID to dependencies
        item_id = "33333333-3333-4333-8333-333333333333"
        content = content.replace("dependencies:\n", f"dependencies:\n  - {item_id}\n")
        task_file.write_text(content, encoding="utf-8")

        validator = Validator(self.root)
        diags = validator.validate_all()
        self_dep_diags = [d for d in diags if "depends on itself" in d.message]
        self.assertEqual(len(self_dep_diags), 1)
        self.assertTrue(self_dep_diags[0].is_fixable)

        # Repair self-dependency
        repairer = Repairer(self.root)
        repairs = repairer.repair()
        self.assertTrue(any("Removed self-dependency" in r for r in repairs))

    def test_cli_check_command(self):
        import io
        from contextlib import redirect_stdout

        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = main(["-C", str(self.root), "check", "--fix"])
        self.assertEqual(ret, 0)
        self.assertIn("Repairs applied:", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
