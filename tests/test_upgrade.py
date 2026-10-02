"""Tests for cache management, download verification, transactional upgrades, and ot upgrade CLI."""

import io
import json
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from ot.cache import (
    ChecksumMismatchError,
    cache_version_artifact,
    get_cached_version_path,
    is_version_cached,
    verify_artifact_checksum,
)
from ot.cli import main
from ot.installation import init_project
from ot.packaging import build_zipapp_artifact, compute_sha256
from ot.upgrade import (
    UpgradeError,
    fetch_version_artifact,
    perform_transactional_upgrade,
)


class TestUpgradeSystem(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.root = Path(self.tmpdir)
        # Use isolated global OT directory for test cache
        os.environ["OT_USER_HOME"] = str(self.root / "global_ot")

    def tearDown(self):
        os.environ.pop("OT_USER_HOME", None)
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_cache_management_and_checksum_verification(self):
        src_dir = Path(__file__).resolve().parent.parent / "src"
        zipapp_file = self.root / "test.zipapp"
        build_zipapp_artifact(src_dir, zipapp_file, "0.2.0")

        # Correct checksum
        sha = compute_sha256(zipapp_file)
        self.assertTrue(verify_artifact_checksum(zipapp_file, sha))

        # Checksum mismatch
        with self.assertRaises(ChecksumMismatchError):
            verify_artifact_checksum(zipapp_file, "bad_checksum_hash_value")

        # Cache artifact
        cached = cache_version_artifact("0.2.0", zipapp_file, expected_sha256=sha)
        self.assertTrue(is_version_cached("0.2.0"))
        self.assertEqual(cached, get_cached_version_path("0.2.0"))

    def test_perform_transactional_upgrade(self):
        proj_dir = self.root / "my_project"
        init_project(proj_dir, version="0.1.0")

        # Upgrade to 0.2.0
        res = perform_transactional_upgrade(proj_dir, "0.2.0")
        self.assertEqual(res["status"], "upgraded")

        # Verify config.json was updated
        cfg = json.loads((proj_dir / ".ot" / "config.json").read_text(encoding="utf-8"))
        self.assertEqual(cfg["system"]["toolVersion"], "0.2.0")

        # Verify binary manifest was updated
        manifest = json.loads((proj_dir / ".ot" / "bin" / "ot-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "0.2.0")

    def test_upgrade_downgrade_rejection(self):
        proj_dir = self.root / "my_project_downgrade"
        init_project(proj_dir, version="0.2.0")

        with self.assertRaises(UpgradeError):
            perform_transactional_upgrade(proj_dir, "0.1.0")

    def test_cli_upgrade_command(self):
        proj_dir = self.root / "cli_upgrade_proj"
        init_project(proj_dir, version="0.1.0")

        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = main(["-C", str(proj_dir), "upgrade", "--version", "0.2.0"])
        self.assertEqual(ret, 0)
        self.assertIn("Successfully upgraded", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
