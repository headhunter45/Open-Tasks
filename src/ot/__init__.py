"""Open Tasks (ot) core package."""

__version__ = "0.1.0"

try:
    import subprocess
    from pathlib import Path

    _git_dir = Path(__file__).resolve().parent.parent.parent / ".git"
    if _git_dir.exists():
        _res = subprocess.run(
            ["git", "describe", "--tags", "--exact-match"],
            capture_output=True,
            text=True,
            timeout=1,
        )
        if _res.returncode == 0:
            _tag = _res.stdout.strip().lstrip("v")
            if _tag:
                __version__ = _tag
except Exception:
    pass
