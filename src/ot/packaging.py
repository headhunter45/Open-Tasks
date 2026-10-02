"""Packaging and release artifact build system for Open Tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any, Dict, List, Optional
import zipapp
import zipfile

from ot.version import is_valid_version


def compute_sha256(file_path: Path | str) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


@dataclass
class ReleaseManifest:
    """Manifest describing a packaged Open Tasks release artifact."""

    version: str
    build_date: str
    sha256: str
    schema_version: int = 1
    artifact_name: str = "ot.zipapp"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "build_date": self.build_date,
            "sha256": self.sha256,
            "schema_version": self.schema_version,
            "artifact_name": self.artifact_name,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ReleaseManifest:
        return cls(
            version=str(data["version"]),
            build_date=str(data.get("build_date", "")),
            sha256=str(data.get("sha256", "")),
            schema_version=int(data.get("schema_version", 1)),
            artifact_name=str(data.get("artifact_name", "ot.zipapp")),
        )


def build_zipapp_artifact(
    src_dir: Path | str,
    output_path: Path | str,
    version: str,
    main_func: str = "ot.cli:main",
) -> ReleaseManifest:
    """Package the `ot` source into a self-contained executable ZipApp (.zipapp).

    Generates manifest.json with SHA-256 checksum and version metadata.
    """
    if not is_valid_version(version):
        raise ValueError(f"Cannot package invalid release version: '{version}'")

    src = Path(src_dir).resolve()
    out = Path(output_path).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as staging_dir:
        staging = Path(staging_dir)

        # Copy the ot package into staging
        ot_src = src / "ot"
        if not ot_src.is_dir():
            raise FileNotFoundError(f"Source package not found at {ot_src}")

        import shutil
        shutil.copytree(ot_src, staging / "ot")

        # Create __main__.py entry point
        main_py = staging / "__main__.py"
        main_py.write_text(
            'import sys\nfrom ot.cli import main\n\nif __name__ == "__main__":\n    sys.exit(main())\n',
            encoding="utf-8",
        )

        # Create zipapp archive with shebang
        zipapp.create_archive(
            staging,
            target=out,
            interpreter="/usr/bin/env python3",
            main=None,  # We created __main__.py
        )

    # Compute SHA-256 checksum
    checksum = compute_sha256(out)
    from ot.models import now_iso

    manifest = ReleaseManifest(
        version=version,
        build_date=now_iso(),
        sha256=checksum,
        artifact_name=out.name,
    )

    # Write manifest alongside artifact
    manifest_path = out.parent / f"{out.stem}-manifest.json"
    manifest_path.write_text(json.dumps(manifest.to_dict(), indent=2), encoding="utf-8")

    return manifest
