# Open Tasks (ot) - Testing and Verification Guide

This guide provides comprehensive instructions for testing, inspecting, and verifying the core Open Tasks engine implemented in Proof of Concept (Tasks **OT-004** through **OT-031**).

---

## 1. Architecture & Feature Overview

The implemented Proof of Concept codebase in [`src/ot/`](src/ot/) provides a database-free, repository-native task tracking architecture:

| Subsystem                  | Components & Modules                                   | Implemented Tasks                                                      |
| :------------------------- | :----------------------------------------------------- | :--------------------------------------------------------------------- |
| **Data Models**            | [`src/ot/models.py`](src/ot/models.py)                 | **OT-004**, **OT-005**, **OT-006**                                     |
| **Examples**               | [`examples/sample-project/`](examples/sample-project/) | **OT-007**                                                             |
| **Discovery**              | [`src/ot/discovery.py`](src/ot/discovery.py)           | **OT-008**, **OT-009**, **OT-010**                                     |
| **Configuration**          | [`src/ot/config.py`](src/ot/config.py)                 | **OT-011**, **OT-012**, **OT-013**                                     |
| **Identifiers**            | [`src/ot/identifiers.py`](src/ot/identifiers.py)       | **OT-014**, **OT-015**, **OT-016**                                     |
| **Parser & Serialization** | [`src/ot/parser.py`](src/ot/parser.py)                 | **OT-017**, **OT-018**, **OT-019**                                     |
| **Scanner & Index**        | [`src/ot/scanner.py`](src/ot/scanner.py)               | **OT-020**, **OT-021**                                                 |
| **CLI Commands**           | [`src/ot/cli.py`](src/ot/cli.py)                       | **OT-022**, **OT-023**, **OT-024**, **OT-025**, **OT-026**, **OT-027** |
| **Validation & Repair**    | [`src/ot/validation.py`](src/ot/validation.py)         | **OT-028**, **OT-029**, **OT-030**                                     |
| **Templates**              | [`src/ot/templates.py`](src/ot/templates.py)           | **OT-031**                                                             |

---

## 2. Automated Test Suite Execution

The repository contains automated unit test suites covering every layer of the architecture.

### Running All Unit Tests

Execute the full test suite from the repository root:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

Expected output:

```text
............................................
----------------------------------------------------------------------
Ran 44 tests in 0.28s

OK
```

### Running Targeted Test Modules

You can run individual test files for specific subsystems:

```bash
# Data models (Metadata, Comments, Relationships)
PYTHONPATH=src python3 -m unittest tests/test_models.py

# Project and VCS discovery
PYTHONPATH=src python3 -m unittest tests/test_discovery.py

# Configuration loader, resolution precedence, and protected keys
PYTHONPATH=src python3 -m unittest tests/test_config.py

# UUID generation, adaptive short prefix IDs, and identifier resolution
PYTHONPATH=src python3 -m unittest tests/test_identifiers.py

# WorkItem reader, atomic writer, and unknown content preservation
PYTHONPATH=src python3 -m unittest tests/test_parser.py

# Repository scanner and in-memory index
PYTHONPATH=src python3 -m unittest tests/test_scanner.py

# CLI commands (task list, show, create, status, comment, dependencies)
PYTHONPATH=src python3 -m unittest tests/test_cli.py

# Validation framework, error diagnostics, and automatic repair
PYTHONPATH=src python3 -m unittest tests/test_validation.py

# Template generator and installation
PYTHONPATH=src python3 -m unittest tests/test_templates.py

# Example project document validation
PYTHONPATH=src python3 -m unittest tests/test_examples.py
```

### Running Legacy Tracker Script Tests

```bash
python3 -m unittest discover -s scripts/tests
```

---

## 3. Interactive CLI Verification Walkthrough

You can interactively test the Open Tasks CLI against the sample project in [`examples/sample-project`](examples/sample-project/).

### Setup Shell Environment

```bash
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"
alias ot="python3 -m ot.cli"
```

---

### Step 1: Listing WorkItems (OT-022)

List all WorkItems discovered in the sample project:

```bash
ot -C examples/sample-project task list
```

**Filter by status:**

```bash
ot -C examples/sample-project task list --status in_progress
```

**Filter by type:**

```bash
ot -C examples/sample-project task list --type bug
```

**JSON output format:**

```bash
ot -C examples/sample-project task list --json
```

---

### Step 2: Inspecting WorkItems & Relationships (OT-023, OT-027)

View complete metadata, parent/child hierarchy, dependencies, blockers, description, and comments:

**By Title:**

```bash
ot -C examples/sample-project task show "Release Alpha"
```

**By Short Prefix:**

```bash
ot -C examples/sample-project task show 111111
```

**Inspect dependency graph:**

```bash
ot -C examples/sample-project task get-dependencies "Fix Login Crash on Null Password"
```

---

### Step 3: Creating a WorkItem (OT-024)

Create a child feature without opening an interactive editor:

```bash
ot -C examples/sample-project task create \
  --title "Add OAuth2 Authentication" \
  --type feature \
  --status planned \
  --size medium \
  --parent "Release Alpha" \
  --overview "Implement OAuth2 login with GitHub and Google providers." \
  --no-edit
```

Verify that the new task is created under `.ot/tasks/ReleaseAlpha/AddOauth2Authentication/index.md` and appears in `ot task list`.

---

### Step 4: Adding Comments (OT-026)

Append an attributed, timestamped comment to a WorkItem:

```bash
ot -C examples/sample-project task comment "Add OAuth2 Authentication" "Requires configuring client IDs in environment."
```

Inspect with `ot task show "Add OAuth2 Authentication"` to verify the rendered markdown comment block.

---

### Step 5: Updating Status (OT-025)

Transition status:

```bash
ot -C examples/sample-project task status "Add OAuth2 Authentication" in_progress
```

---

### Step 6: Managing Dependencies (OT-027)

Declare that `Add OAuth2 Authentication` depends on `Implement User Authentication`:

```bash
ot -C examples/sample-project task add-dependency "Add OAuth2 Authentication" "Implement User Authentication"
```

Verify dependencies:

```bash
ot -C examples/sample-project task get-dependencies "Add OAuth2 Authentication"
```

Remove dependency:

```bash
ot -C examples/sample-project task remove-dependency "Add OAuth2 Authentication" "Implement User Authentication"
```

---

### Step 7: Project Validation & Auto-Repair (OT-028, OT-029, OT-030)

Run full project integrity check:

```bash
ot -C examples/sample-project check
```

**JSON diagnostic report:**

```bash
ot -C examples/sample-project check --json
```

**Validate and automatically repair fixable issues (missing folders, misplaced protected config keys, self-dependencies):**

```bash
ot -C examples/sample-project check --fix
```

---

### Step 8: Template Verification (OT-031)

Inspect installed templates in `examples/sample-project/.ot/templates/`:

- `tasks/default.md`, `tasks/bug.md`, `tasks/feature.md`, `tasks/epic.md`, `tasks/chore.md`, `tasks/spike.md`
- `meetings/grooming.md`, `meetings/planning.md`, `meetings/retrospective.md`, `meetings/ideation.md`
- `shared/comment.md`

---

## 4. Verification Checklist

- [x] All 44 automated tests in `tests/` pass with exit code 0.
- [x] `ot task list` correctly discovers and indexes nested `.ot/tasks/` hierarchies.
- [x] Identifier resolution works seamlessly with full UUIDs, short prefixes, and titles.
- [x] Lossless round-tripping preserves custom frontmatter and markdown sections.
- [x] Multi-tier configuration resolves precedence order cleanly without side effects.
- [x] `ot check` reports actionable diagnostics and `ot check --fix` performs safe deterministic repairs.
