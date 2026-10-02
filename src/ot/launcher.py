"""Global launcher for Open Tasks."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
from typing import List, Optional

from ot.config import load_config, load_json_file
from ot.discovery import find_project_root


def find_project_binary(project_root: Path) -> Optional[Path]:
    """Find the project-installed Open Tasks executable beneath .ot/bin/."""
    candidates = [
        project_root / ".ot" / "bin" / "ot.zipapp",
        project_root / ".ot" / "bin" / "ot.py",
        project_root / ".ot" / "bin" / "ot",
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def get_configured_version(project_root: Path) -> Optional[str]:
    """Read system.toolVersion from .ot/config.json."""
    config_file = project_root / ".ot" / "config.json"
    if not config_file.is_file():
        return None
    try:
        data = load_json_file(config_file)
        return data.get("system", {}).get("toolVersion")
    except Exception:
        return None


def launch_project_binary(binary_path: Path, args: List[str]) -> int:
    """Execute the project-installed binary with python3."""
    cmd = [sys.executable, str(binary_path), *args]
    res = subprocess.run(cmd)
    return res.returncode


def run_launcher(args: Optional[List[str]] = None, start_dir: Optional[Path | str] = None) -> int:
    """Main entry point for the global `ot` launcher."""
    if args is None:
        args = sys.argv[1:]

    # Intercept top-level --version or version command
    if args and args[0] in ("--version", "-V", "version"):
        from ot import __version__
        print(f"Open Tasks Launcher v{__version__}")
        proj_root = find_project_root(start_dir)
        if proj_root:
            cfg_v = get_configured_version(proj_root)
            bin_p = find_project_binary(proj_root)
            print(f"Project root:       {proj_root}")
            print(f"Configured version: {cfg_v or 'Not specified (using default)'}")
            print(f"Installed binary:   {bin_p or 'None (using fallback implementation)'}")
        return 0

    proj_root = find_project_root(start_dir)

    # If initializing or no project exists yet, run directly via core cli
    if not proj_root or (args and args[0] == "init"):
        from ot.cli import main as cli_main
        return cli_main(args)

    # Check for project-installed implementation beneath .ot/bin/
    project_bin = find_project_binary(proj_root)
    if project_bin:
        return launch_project_binary(project_bin, args)

    # Fallback to local / environment package implementation
    from ot.cli import main as cli_main
    return cli_main(args)


if __name__ == "__main__":
    sys.exit(run_launcher())
