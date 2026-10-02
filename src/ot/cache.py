"""Cache management and download verification for Open Tasks."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
from typing import Optional

from ot.packaging import compute_sha256
from ot.version import is_valid_version


class ChecksumMismatchError(ValueError):
    """Raised when downloaded artifact checksum does not match expected SHA-256."""
    pass


def get_global_ot_dir() -> Path:
    """Return ~/.ot directory path."""
    p = Path(os.getenv("OT_USER_HOME") or "~/.ot").expanduser().resolve()
    p.mkdir(parents=True, exist_ok=True)
    return p


def get_cache_dir() -> Path:
    """Return ~/.ot/cache/ directory path."""
    d = get_global_ot_dir() / "cache"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_versions_cache_dir() -> Path:
    """Return ~/.ot/versions/ directory path."""
    d = get_global_ot_dir() / "versions"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_cached_version_path(version: str) -> Path:
    """Return the cached zipapp path for a version in ~/.ot/versions/<version>/ot.zipapp."""
    return get_versions_cache_dir() / version / "ot.zipapp"


def is_version_cached(version: str) -> bool:
    """Check if version artifact is present in local cache."""
    return get_cached_version_path(version).is_file()


def verify_artifact_checksum(artifact_path: Path | str, expected_sha256: str) -> bool:
    """Verify that file's SHA-256 matches expected checksum.

    Raises ChecksumMismatchError on mismatch.
    """
    actual = compute_sha256(artifact_path)
    if actual.lower() != expected_sha256.strip().lower():
        raise ChecksumMismatchError(
            f"Checksum mismatch for {artifact_path}: expected {expected_sha256}, got {actual}"
        )
    return True


def cache_version_artifact(
    version: str,
    artifact_path: Path | str,
    expected_sha256: Optional[str] = None,
) -> Path:
    """Store an artifact into ~/.ot/versions/<version>/ot.zipapp after checksum verification."""
    if not is_valid_version(version):
        raise ValueError(f"Invalid version string: '{version}'")

    src = Path(artifact_path).resolve()
    if not src.is_file():
        raise FileNotFoundError(f"Source artifact not found: {src}")

    if expected_sha256:
        verify_artifact_checksum(src, expected_sha256)

    dest_dir = get_versions_cache_dir() / version
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_zipapp = dest_dir / "ot.zipapp"

    shutil.copy2(src, dest_zipapp)

    # Save manifest
    manifest_data = {
        "version": version,
        "sha256": compute_sha256(dest_zipapp),
    }
    (dest_dir / "ot-manifest.json").write_text(json.dumps(manifest_data, indent=2), encoding="utf-8")

    return dest_zipapp
