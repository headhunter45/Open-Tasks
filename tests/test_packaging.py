"""Tests for packaging, versioning, and release artifacts."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from ot.packaging import (
    ReleaseManifest,
    build_zipapp_artifact,
    compute_sha256,
)
from ot.version import (
    compare_versions,
    is_valid_version,
    parse_semver,
)


class TestVersioningAndPackaging(unittest.TestCase):
    def test_semver_parsing_and_comparison(self):
        self.assertTrue(is_valid_version("1.0.0"))
        self.assertTrue(is_valid_version("0.1.0-alpha"))
        self.assertFalse(is_valid_version("1.0"))
        self.assertFalse(is_valid_version("abc"))

        self.assertEqual(compare_versions("1.0.0", "1.0.0"), 0)
        self.assertEqual(compare_versions("1.0.0", "1.1.0"), -1)
        self.assertEqual(compare_versions("2.0.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.0.0-alpha", "1.0.0"), -1)

    def test_build_zipapp_artifact(self):
        src_dir = Path(__file__).resolve().parent.parent / "src"
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = Path(tmpdir) / "dist" / "ot.zipapp"
            manifest = build_zipapp_artifact(src_dir, out_path, "0.1.0")

            self.assertTrue(out_path.is_file())
            self.assertEqual(manifest.version, "0.1.0")
            self.assertEqual(manifest.sha256, compute_sha256(out_path))

            # Test executing the packaged zipapp via python3
            res = subprocess.run(
                ["python3", str(out_path), "--help"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(res.returncode, 0)
            self.assertIn("Open Tasks", res.stdout)


if __name__ == "__main__":
    unittest.main()
