"""Tests for ot init and project installation."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from ot.cli import main
from ot.installation import init_project


class TestInstallationAndInit(unittest.TestCase):
    def test_init_project_function(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            res = init_project(
                target_dir=tmpdir,
                project_name="Demo Init",
                version="0.1.0",
                description="Demo project",
                install_binary=True,
                create_wrappers=True,
            )
            root = Path(tmpdir)
            self.assertTrue((root / ".ot").is_dir())
            self.assertTrue((root / ".ot" / "config.json").is_file())
            self.assertTrue((root / ".ot" / "templates" / "tasks" / "default.md").is_file())
            self.assertTrue((root / ".ot" / "bin" / "ot.zipapp").is_file())
            self.assertTrue((root / "otw").is_file())

            cfg_data = json.loads((root / ".ot" / "config.json").read_text(encoding="utf-8"))
            self.assertEqual(cfg_data["system"]["toolVersion"], "0.1.0")
            self.assertEqual(cfg_data["project"]["name"], "Demo Init")

    def test_cli_init_command(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            buf = io.StringIO()
            with redirect_stdout(buf):
                ret = main(["init", tmpdir, "--name", "CLI Project", "--version", "0.1.0"])
            self.assertEqual(ret, 0)
            self.assertIn("Initialized Open Tasks project", buf.getvalue())
            self.assertTrue((Path(tmpdir) / ".ot" / "config.json").is_file())


if __name__ == "__main__":
    unittest.main()
