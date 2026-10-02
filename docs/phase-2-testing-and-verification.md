# Open Tasks (ot) - Phase 2 Testing and Verification Guide

This guide provides comprehensive instructions for testing, inspecting, and verifying the **Distribution and Release System** implemented in Phase 2 (Tasks **OT-032** through **OT-044**).

---

## 1. Architecture & Feature Overview

The Phase 2 distribution subsystem in [`src/ot/`](file:///Users/tom/Projects/OpenTasks/src/ot/) provides an end-to-end release, launcher, installation, and upgrade mechanism:

| Subsystem | Components & Modules | Implemented Tasks |
| :--- | :--- | :--- |
| **Release Artifact** | [`src/ot/packaging.py`](file:///Users/tom/Projects/OpenTasks/src/ot/packaging.py) | **OT-032** |
| **Packaging System** | [`src/ot/packaging.py`](file:///Users/tom/Projects/OpenTasks/src/ot/packaging.py), [`scripts/package-release`](file:///Users/tom/Projects/OpenTasks/scripts/package-release) | **OT-033** |
| **Global Launcher** | [`src/ot/launcher.py`](file:///Users/tom/Projects/OpenTasks/src/ot/launcher.py) | **OT-034** |
| **Version Discovery** | [`src/ot/version.py`](file:///Users/tom/Projects/OpenTasks/src/ot/version.py) | **OT-035** |
| **Version Validation** | [`src/ot/version.py`](file:///Users/tom/Projects/OpenTasks/src/ot/version.py), [`src/ot/validator.py`](file:///Users/tom/Projects/OpenTasks/src/ot/validator.py) | **OT-036** |
| **Project Initialization** | [`src/ot/installation.py`](file:///Users/tom/Projects/OpenTasks/src/ot/installation.py), [`src/ot/cli.py`](file:///Users/tom/Projects/OpenTasks/src/ot/cli.py) | **OT-037** |
| **Project Installation & Wrappers** | [`src/ot/installation.py`](file:///Users/tom/Projects/OpenTasks/src/ot/installation.py) | **OT-038** |
| **Version Downloads & Staging** | [`src/ot/upgrade.py`](file:///Users/tom/Projects/OpenTasks/src/ot/upgrade.py), [`src/ot/cache.py`](file:///Users/tom/Projects/OpenTasks/src/ot/cache.py) | **OT-039** |
| **Transactional Upgrades** | [`src/ot/upgrade.py`](file:///Users/tom/Projects/OpenTasks/src/ot/upgrade.py) | **OT-040** |
| **CLI Upgrade Command** | [`src/ot/cli.py`](file:///Users/tom/Projects/OpenTasks/src/ot/cli.py) | **OT-041** |
| **Cache Management** | [`src/ot/cache.py`](file:///Users/tom/Projects/OpenTasks/src/ot/cache.py) | **OT-042** |
| **Download Verification** | [`src/ot/cache.py`](file:///Users/tom/Projects/OpenTasks/src/ot/cache.py) | **OT-043** |
| **Release Pipeline** | [`scripts/build-release`](file:///Users/tom/Projects/OpenTasks/scripts/build-release) | **OT-044** |

---

## 2. Automated Test Suite Execution

The repository contains automated unit test suites covering the distribution, packaging, installation, versioning, and upgrade systems.

### Running All Unit Tests

Execute the full unit test suite from the repository root:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

Expected output:
```text
.......................................................
----------------------------------------------------------------------
Ran 55 tests in 0.82s

OK
```

### Running Targeted Distribution Test Modules

You can run individual test suites for specific distribution components:

```bash
# Packaging & ZipApp artifact generation (OT-032, OT-033)
PYTHONPATH=src python3 -m unittest tests/test_packaging.py

# Global launcher & version discovery delegation (OT-034)
PYTHONPATH=src python3 -m unittest tests/test_launcher.py

# Version discovery, SemVer parsing & validation (OT-035, OT-036)
PYTHONPATH=src python3 -m unittest tests/test_version.py

# Repository initialization & wrapper generation (OT-037, OT-038)
PYTHONPATH=src python3 -m unittest tests/test_installation.py

# Transactional upgrade engine & rollback (OT-039, OT-040, OT-041)
PYTHONPATH=src python3 -m unittest tests/test_upgrade.py

# Cache management & SHA-256 integrity verification (OT-042, OT-043)
PYTHONPATH=src python3 -m unittest tests/test_cache.py
```

### Running Legacy Tracker Script Tests

```bash
python3 -m unittest discover -s scripts/tests
```

---

## 3. Interactive CLI & Distribution Verification Walkthrough

Follow these steps to manually verify the release build, launcher, project initialization, wrapper scripts, and upgrade workflow.

### Setup Shell Environment

```bash
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"
```

---

### Step 1: Packaging a Release Artifact (OT-032, OT-033)

Build a standalone, executable `.zipapp` release bundle:

```bash
./scripts/package-release --version 0.1.0 --output dist/ot-0.1.0.zipapp
```

Verify the generated output files in `dist/`:
```bash
ls -lh dist/
# Should contain:
# - ot-0.1.0.zipapp (standalone executable Python zipapp)
# - ot-0.1.0.manifest.json (release metadata with sha256 checksum)
# - ot-0.1.0.zipapp.sha256 (checksum file)
```

Directly execute the created `.zipapp`:
```bash
./dist/ot-0.1.0.zipapp --version
```

---

### Step 2: Automated Release Pipeline (OT-044)

Run the full end-to-end release pipeline script (runs test suite, builds artifacts, verifies checksums, and tests artifact execution):

```bash
./scripts/build-release --version 0.1.0 --output-dir dist
```

---

### Step 3: Initializing a New Project (OT-037, OT-038)

Create a temporary test directory and initialize Open Tasks within it:

```bash
# Create a test directory
mkdir -p /tmp/ot-demo-project
cd /tmp/ot-demo-project

# Initialize Open Tasks with bundled zipapp and wrappers
python3 -m ot.cli init --name "Demo Project" --bundle-zipapp
```

Verify that the initialization created:
- `.ot/config.json` containing project metadata and version `0.1.0`
- `.ot/bin/ot.zipapp` containing the executable binary
- `.ot/templates/` with default task and meeting templates
- `otw` (Unix wrapper script) and `otw.bat` (Windows wrapper script)

Test invoking Open Tasks via the project wrapper:
```bash
./otw version
./otw task list
```

---

### Step 4: Version Discovery and Validation (OT-035, OT-036)

Check project and installed versions:

```bash
./otw version
```

Output:
```text
Project configured version: 0.1.0
Installed binary version:   0.1.0
```

Run project validation (`ot check`) to ensure version consistency:
```bash
./otw check
```

---

### Step 5: Global Launcher Execution (OT-034)

Test the global launcher detecting and delegating to the project's installed `.ot/bin/ot.zipapp`:

```bash
# Run launcher from inside the project directory
python3 -m ot.launcher task list

# Run launcher from a subdirectory
mkdir -p sub/nested/dir
cd sub/nested/dir
python3 -m ot.launcher version
cd /tmp/ot-demo-project
```

---

### Step 6: Transactional Upgrade Verification (OT-039, OT-040, OT-041)

Package a newer version `0.2.0` in the repository root:

```bash
cd /Users/tom/Projects/OpenTasks
./scripts/package-release --version 0.2.0 --output dist/ot-0.2.0.zipapp
```

Test upgrading the demo project to `0.2.0`:

```bash
cd /tmp/ot-demo-project
# Upgrade using the newly packaged version artifact
python3 -m ot.cli upgrade --version 0.2.0 --artifact /Users/tom/Projects/OpenTasks/dist/ot-0.2.0.zipapp
```

Verify:
1. `config.json` updated `version` to `"0.2.0"`.
2. `.ot/bin/ot.zipapp` updated to the `0.2.0` binary.
3. Existing custom templates or task files were safely preserved.
4. `./otw version` now outputs `0.2.0`.

---

### Step 7: Cache Management & Download Verification (OT-042, OT-043)

Verify cached versions stored under `~/.ot/cache/` and `~/.ot/versions/`:

```python
python3 -c "
from ot.cache import CacheManager
cm = CacheManager()
print('Cached downloads:', cm.list_cached_downloads())
print('Installed versions:', cm.list_cached_versions())
"
```

Clean up temporary verification directory:
```bash
rm -rf /tmp/ot-demo-project
```

---

## 4. Verification Checklist

- [x] Standalone executable `zipapp` format runs cleanly on any standard Python 3.10+ runtime without external dependencies.
- [x] `scripts/package-release` produces deterministic `.zipapp` artifacts, `.manifest.json`, and `.sha256` checksums.
- [x] Global launcher automatically discovers the nearest `.ot/` root and delegates execution to `.ot/bin/ot.zipapp`.
- [x] `ot init` creates project structure, starter templates, executable binary, and `otw`/`otw.bat` wrappers.
- [x] `ot check` validates SemVer compatibility and flags version mismatches.
- [x] `ot upgrade` performs atomic, non-destructive upgrades with isolated staging and automatic rollback on failure.
- [x] SHA-256 verification rejects corrupt or tampered release artifacts before installation.
- [x] `scripts/build-release` automates test suite execution, packaging, manifest generation, and post-build artifact verification.
- [x] All 55 automated unit tests in `tests/` pass with exit code 0.
