"""Project initialization and tool installation for Open Tasks."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
from typing import Any, Dict, Optional

from ot import __version__ as DEFAULT_LAUNCHER_VERSION
from ot.config import DEFAULT_CONFIG
from ot.packaging import ReleaseManifest, build_zipapp_artifact, compute_sha256
from ot.templates import install_default_templates
from ot.version import is_valid_version


WRAPPER_SCRIPT_SH = """#!/usr/bin/env bash
set -euo pipefail
PROJ_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN="${PROJ_ROOT}/.ot/bin/ot.zipapp"

if [ -f "$BIN" ]; then
    exec python3 "$BIN" "$@"
else
    exec ot "$@"
fi
"""

WRAPPER_SCRIPT_BAT = """@echo off
set "PROJ_ROOT=%~dp0"
set "BIN=%PROJ_ROOT%.ot\\bin\\ot.zipapp"

if exist "%BIN%" (
    python "%BIN%" %*
) else (
    ot %*
)
"""


def install_project_binary(
    project_root: Path,
    version: str,
    src_dir: Optional[Path | str] = None,
) -> Path:
    """Install Open Tasks executable zipapp and manifest into .ot/bin/."""
    bin_dir = project_root / ".ot" / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)
    out_zipapp = bin_dir / "ot.zipapp"

    # If src_dir is provided or exists, build directly; otherwise locate package
    if not src_dir:
        # Check current repo src or package root
        candidate = Path(__file__).resolve().parent.parent
        if (candidate / "ot").is_dir():
            src_dir = candidate
        else:
            src_dir = Path(__file__).resolve().parent.parent.parent / "src"

    build_zipapp_artifact(src_dir, out_zipapp, version)
    return out_zipapp


def init_project(
    target_dir: Path | str,
    project_name: Optional[str] = None,
    version: Optional[str] = None,
    description: str = "",
    install_binary: bool = True,
    create_wrappers: bool = True,
) -> Dict[str, Any]:
    """Initialize a new Open Tasks project in target_dir."""
    root = Path(target_dir).resolve()
    ot_dir = root / ".ot"
    ot_dir.mkdir(parents=True, exist_ok=True)

    # 1. Create directory structure
    for sub in ["tasks", "meetings", "templates", "bin"]:
        (ot_dir / sub).mkdir(parents=True, exist_ok=True)

    tool_version = version or DEFAULT_LAUNCHER_VERSION
    if not is_valid_version(tool_version):
        raise ValueError(f"Invalid version for initialization: '{tool_version}'")

    proj_name = project_name or root.name

    # 2. Generate .ot/config.json
    config_data = json.loads(json.dumps(DEFAULT_CONFIG))
    config_data["system"]["toolVersion"] = tool_version
    config_data["project"]["name"] = proj_name
    config_data["project"]["description"] = description

    config_path = ot_dir / "config.json"
    if not config_path.exists():
        config_path.write_text(json.dumps(config_data, indent=2), encoding="utf-8")

    # 3. Install default templates
    templates_count = install_default_templates(root)

    # 4. Install project binary
    binary_path = None
    if install_binary:
        binary_path = install_project_binary(root, tool_version)

    # 5. Create wrapper scripts
    if create_wrappers:
        otw = root / "otw"
        if not otw.exists():
            otw.write_text(WRAPPER_SCRIPT_SH, encoding="utf-8")
            otw.chmod(0o755)
        otw_bat = root / "otw.bat"
        if not otw_bat.exists():
            otw_bat.write_text(WRAPPER_SCRIPT_BAT, encoding="utf-8")

    return {
        "project_root": root,
        "name": proj_name,
        "version": tool_version,
        "templates_count": templates_count,
        "binary_path": binary_path,
    }
