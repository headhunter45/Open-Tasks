# Open Tasks (ot) - Phase 3 Testing and Verification Guide

This guide provides comprehensive instructions for testing, inspecting, and verifying the **Self Hosting and Bootstrap System** implemented in Phase 3 (Tasks **OT-045** through **OT-059**).

---

## 1. Architecture & Feature Overview

The Phase 3 subsystem enables Open Tasks to manage its own development lifecycle in a fully self-hosted, repository-native environment:

| Subsystem | Components & Modules | Implemented Tasks |
| :--- | :--- | :--- |
| **Self-Hosting Initialization** | [`.ot/config.json`](file:///Users/tom/Projects/OpenTasks/.ot/config.json), [`.ot/bin/ot.zipapp`](file:///Users/tom/Projects/OpenTasks/.ot/bin/ot.zipapp), [`otw`](file:///Users/tom/Projects/OpenTasks/otw), [`otw.bat`](file:///Users/tom/Projects/OpenTasks/otw.bat) | **OT-045** |
| **WorkItem Templates** | [`.ot/templates/tasks/`](file:///Users/tom/Projects/OpenTasks/.ot/templates/tasks/) (`feature.md`, `bug.md`, `epic.md`, `chore.md`, `spike.md`, `default.md`) | **OT-046** |
| **Meeting Templates** | [`.ot/templates/meetings/`](file:///Users/tom/Projects/OpenTasks/.ot/templates/meetings/) (`grooming.md`, `planning.md`, `retrospective.md`, `ideation.md`) | **OT-047** |
| **Initial Backlog** | [`.ot/tasks/`](file:///Users/tom/Projects/OpenTasks/.ot/tasks/) (`ExportAndReportingTooling`, `MercurialVcsIntegration`, `JsonSchemaExport`) | **OT-048** |
| **Task Migration** | [`.ot/tasks/ProofOfConcept/`](file:///Users/tom/Projects/OpenTasks/.ot/tasks/ProofOfConcept/), [`.ot/tasks/DistributionAndReleaseSystem/`](file:///Users/tom/Projects/OpenTasks/.ot/tasks/DistributionAndReleaseSystem/), [`.ot/tasks/SelfHostingAndBootstrap/`](file:///Users/tom/Projects/OpenTasks/.ot/tasks/SelfHostingAndBootstrap/) | **OT-049** |
| **Migration Validation** | [`src/ot/validation.py`](file:///Users/tom/Projects/OpenTasks/src/ot/validation.py), `ot check` | **OT-050** |
| **WorkItem Creation** | `ot task create` / `./otw task create` | **OT-051** |
| **Lifecycle & Status Updates** | `ot task status`, `ot task comment`, `ot task add-dependency`, `ot task edit` | **OT-052** |
| **Legacy Script Retirement** | [`scripts/README.md`](file:///Users/tom/Projects/OpenTasks/scripts/README.md) | **OT-053** |
| **Legacy Tracker Archival** | [`docs/tasks.md`](file:///Users/tom/Projects/OpenTasks/docs/tasks.md) Archival Notice | **OT-054** |
| **Backlog Grooming** | [`.ot/meetings/2026-10-02-grooming.md`](file:///Users/tom/Projects/OpenTasks/.ot/meetings/2026-10-02-grooming.md) | **OT-055** |
| **Meeting Notes Recording** | [`.ot/meetings/2026-10-02-grooming.md`](file:///Users/tom/Projects/OpenTasks/.ot/meetings/2026-10-02-grooming.md) | **OT-056** |
| **Release Planning** | [`.ot/meetings/2026-10-02-release-0.1.0-plan.md`](file:///Users/tom/Projects/OpenTasks/.ot/meetings/2026-10-02-release-0.1.0-plan.md), `Release v0.1.0` WorkItem | **OT-057** |
| **Development Workflow** | `./otw`, `ot version`, `ot check`, `scripts/build-release` | **OT-058** |
| **Bootstrap Completion** | Full milestone validation, parent epic OT-003 completion | **OT-059** |

---

## 2. Automated Test Suite Execution

Run the complete test suite to verify core engines, packaging, installation, validation, and legacy script compatibility.

### Running All Unit Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

Expected output:
```text
.......................................................
----------------------------------------------------------------------
Ran 55 tests in 0.75s

OK
```

### Running Script & Legacy Tooling Tests

```bash
python3 -m unittest discover -s scripts/tests
```

Expected output:
```text
...........
----------------------------------------------------------------------
Ran 11 tests in 3.40s

OK
```

---

## 3. Interactive Self-Hosting & Verification Walkthrough

Follow these steps to manually verify the self-hosted Open Tasks environment, task migration, CLI operations, and release pipeline.

### Step 1: Verify Self-Hosted Project Version & Health (OT-045, OT-050)

Run project diagnostic checks using the self-hosted project wrapper script:

```bash
# Check version reporting
./otw version
```

Expected output:
```text
Open Tasks v0.1.0
Project root:       /Users/tom/Projects/OpenTasks
Configured version: 0.1.0
Installed version:  0.1.0
```

Run project integrity validation:
```bash
./otw check
```

Expected output:
```text
Project check passed: No errors or warnings detected.
```

JSON diagnostic output verification:
```bash
./otw check --json
# Output should be: []
```

---

### Step 2: Querying Migrated Backlog Items (OT-048, OT-049)

List all migrated and active work items in the repository:

```bash
./otw task list
```

**Filter by status:**
```bash
# View completed work items
./otw task list --status completed

# View planned backlog items
./otw task list --status planned
```

**Filter by type:**
```bash
# View high-level epics
./otw task list --type epic
```

**Inspect a specific migrated task:**
```bash
./otw task show "Define WorkItem Metadata"
```

---

### Step 3: Creating a WorkItem with Templates (OT-046, OT-051)

Create a new feature task under the self-hosted project:

```bash
./otw task create \
  --title "Interactive Dashboard UI" \
  --type feature \
  --status planned \
  --size large \
  --parent "Export and Reporting Tooling" \
  --overview "Provide an optional terminal dashboard for live task statistics." \
  --no-edit
```

Verify that the task is created with appropriate template sections under `.ot/tasks/ExportAndReportingTooling/InteractiveDashboardUi/index.md`.

---

### Step 4: Updating Task Lifecycles (OT-052)

Transition status, append comments, and link dependencies:

```bash
# Update status
./otw task status "Interactive Dashboard UI" in_progress

# Add timestamped attributed comment
./otw task comment "Interactive Dashboard UI" "Evaluating textual/rich UI libraries for Python terminal rendering."

# Declare a dependency
./otw task add-dependency "Interactive Dashboard UI" "JSON Schema Export"

# Inspect the updated work item
./otw task show "Interactive Dashboard UI"
```

---

### Step 5: Meeting Records & Planning (OT-047, OT-055, OT-056, OT-057)

Inspect recorded meeting notes in `.ot/meetings/`:

```bash
cat .ot/meetings/2026-10-02-grooming.md
cat .ot/meetings/2026-10-02-release-0.1.0-plan.md
```

Verify meeting frontmatter structure (`type`, `date`, `attendees`) and markdown agenda/action items.

---

### Step 6: Full Release Build & Checksum Verification (OT-058)

Execute the production release pipeline to produce and verify standalone distribution binaries:

```bash
./scripts/build-release --version 0.1.0
```

Verify that the output directory `dist/` contains:
- `ot-0.1.0.zipapp`
- `ot.zipapp`
- `ot-0.1.0-manifest.json`
- `SHA256SUMS`

Test the standalone distribution binary directly:
```bash
python3 dist/ot-0.1.0.zipapp version
python3 dist/ot-0.1.0.zipapp task list
```

---

### Step 7: Clean Up Verification Scratch Items

Clean up the test task created in Step 3:
```bash
rm -rf .ot/tasks/ExportAndReportingTooling/InteractiveDashboardUi
./otw check
```

---

## 4. Verification Checklist

- [x] Repository is self-hosted with `.ot/`, `config.json`, `.ot/bin/ot.zipapp`, and `./otw` wrapper script.
- [x] All 6 WorkItem templates and 4 meeting templates installed and functional in `.ot/templates/`.
- [x] All 59 historical tasks and epics successfully migrated into `.ot/tasks/` hierarchy.
- [x] `ot check` / `otw check` passes with 0 diagnostics.
- [x] New tasks can be created, updated, commented, and linked via `otw task` commands.
- [x] Legacy single-file tracker archived and retirement documented in `scripts/README.md`.
- [x] Grooming and release planning meeting notes recorded under `.ot/meetings/`.
- [x] Automated release pipeline builds, packages, and validates standalone `.zipapp` artifacts.
- [x] All 55 core tests and 11 tracker script tests pass with exit code 0.
