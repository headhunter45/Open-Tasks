"""Project and VCS discovery for Open Tasks."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
from typing import Optional, Tuple


def find_project_root(start_dir: Optional[Path | str] = None) -> Optional[Path]:
    """Find the Open Tasks project root containing `.ot`.

    Traverses upwards from `start_dir` (defaulting to cwd).
    Also checks OPEN_TASKS_ROOT or OT_ROOT environment variables if set.
    """
    env_root = os.getenv("OPEN_TASKS_ROOT") or os.getenv("OT_ROOT")
    if env_root:
        p = Path(env_root).resolve()
        if (p / ".ot").is_dir():
            return p

    current = Path(start_dir or Path.cwd()).resolve()
    # If a file was passed, start from its parent
    if current.is_file():
        current = current.parent

    for parent in [current, *current.parents]:
        if (parent / ".ot").is_dir():
            return parent

    return None


def find_vcs_root(start_dir: Optional[Path | str] = None) -> Tuple[Optional[str], Optional[Path]]:
    """Find the root of the containing Version Control System (.git or .hg).

    Returns:
        (vcs_type, root_path) where vcs_type is 'git', 'hg', or None.
    """
    current = Path(start_dir or Path.cwd()).resolve()
    if current.is_file():
        current = current.parent

    for parent in [current, *current.parents]:
        if (parent / ".git").exists():
            return "git", parent
        if (parent / ".hg").exists():
            return "hg", parent

    return None, None


def discover_root(start_dir: Optional[Path | str] = None, allow_fallback: bool = True) -> Path:
    """Discover the project root using standard priority:
    1. .ot directory
    2. .git root (if .ot not yet created)
    3. .hg root
    4. Current directory (if allow_fallback is True)
    """
    proj_root = find_project_root(start_dir)
    if proj_root:
        return proj_root

    vcs_type, vcs_root = find_vcs_root(start_dir)
    if vcs_root:
        return vcs_root

    if allow_fallback:
        current = Path(start_dir or Path.cwd()).resolve()
        return current.parent if current.is_file() else current

    raise FileNotFoundError("Could not locate Open Tasks project root (.ot).")
