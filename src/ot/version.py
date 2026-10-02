"""Version and semver validation utilities for Open Tasks."""

from __future__ import annotations

import re
from typing import Optional, Tuple

VERSION_PATTERN = re.compile(
    r"^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?(?:\+([0-9A-Za-z.-]+))?$"
)


def parse_semver(v_str: str) -> Tuple[int, int, int, str]:
    """Parse a semantic version string into (major, minor, patch, prerelease)."""
    clean = v_str.strip().lstrip("v")
    m = VERSION_PATTERN.match(clean)
    if not m:
        raise ValueError(f"Invalid semantic version string: '{v_str}'")
    major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    prerelease = m.group(4) or ""
    return major, minor, patch, prerelease


def is_valid_version(v_str: str) -> bool:
    """Check if version string is a valid semantic version."""
    try:
        parse_semver(v_str)
        return True
    except ValueError:
        return False


def compare_versions(v1: str, v2: str) -> int:
    """Compare two semantic versions.

    Returns:
        -1 if v1 < v2
         0 if v1 == v2
         1 if v1 > v2
    """
    maj1, min1, pat1, pre1 = parse_semver(v1)
    maj2, min2, pat2, pre2 = parse_semver(v2)

    t1 = (maj1, min1, pat1)
    t2 = (maj2, min2, pat2)
    if t1 < t2:
        return -1
    if t1 > t2:
        return 1

    # Same major.minor.patch: prerelease is lower than release
    if pre1 and not pre2:
        return -1
    if not pre1 and pre2:
        return 1
    if pre1 < pre2:
        return -1
    if pre1 > pre2:
        return 1
    return 0
