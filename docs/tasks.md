---
task-id-prefix: 'OT'
projects:
  - label: 'Open Tasks'
    path: '.'
    prefix: 'OT'
    value: 'open-tasks'
epics:
  - value: 'poc'
    label: 'Proof of Concept'
    description: 'Validate the core architecture and WorkItem model.'
  - value: 'distribution'
    label: 'Distribution and Release System'
    description: 'Enable installation, upgrades, packaging, release workflows, and project version management.'
  - value: 'bootstrap'
    label: 'Self Hosting and Bootstrap'
    description: 'Migrate development onto Open Tasks and retire the legacy tracker.'
task-statuses:
  - value: 'planning'
    label: 'Planning'
    description: "The task is being scoped and conceptualized. We still don't know what we want."
  - value: 'triage'
    label: 'Triage'
    description: "The task is being evaluated and prioritized. We don't know how we want to do it."
  - value: 'pending'
    label: 'Pending'
    description: 'The task is ready to be acted on.'
  - value: 'in_progress'
    label: 'In Progress'
    description: 'The task is currently being worked on.'
  - value: 'done'
    label: 'Fixed'
    description: 'The task has been completed.'
  - value: 'blocked'
    label: 'Blocked'
    description: 'The task cannot proceed due to an obstacle or dependency.'
  - value: 'cancelled'
    label: 'Cancelled'
    description: 'The task was decided against or is no longer relevant.'
  - value: 'research'
    label: 'Researching'
    description: 'This task needs more research before planning.'
task-types:
  - value: 'lint'
    prefix: 'LNT'
    label: 'Lint'
    description: 'The task involves fixing a linting error or other warning.'
  - value: 'bug'
    prefix: 'BUG'
    label: 'Bug'
    description: 'The task is a bug to fix.'
  - value: 'feature'
    prefix: 'ENH'
    label: 'Feature'
    description: 'The task is a new feature to implement.'
  - value: 'chore'
    prefix: 'CHR'
    label: 'Chore'
    description: 'The task is a routine maintenance or administrative task.'
---

# Project Task Tracker (Archived)

> [!NOTE]
> **ARCHIVED**: This single-file tracker document has been archived. Open Tasks is now fully self-hosted! All work items and epics are maintained directly in repository-native files under [`.ot/tasks/`](.ot/tasks/) and managed via `./otw` or the `ot` CLI.

This document serves as the historical record for bootstrap and initial project phases.

## Instructions for Working with Tasks

### Quick Start (Environment Setup)

Before running task commands, source the helper environment script in your shell to load convenient aliases and paths:

```bash
source ./scripts/env.sh
```

### Task ID Configuration

- Set the document-wide `task-id-prefix` in YAML frontmatter (this tracker uses `OT`).
- Optionally export `TASK_ID_PREFIX` in your shell or in the local settings sourced by `scripts/env.sh` (`scripts/env.sh.local` or `.env`). It overrides frontmatter; when neither is set, the default is `OT`.
- Prefixes must start with a letter and contain only letters, digits, underscores, or hyphens. Display IDs are uppercase and anchors are lowercase.
- Numbers remain globally monotonic across the document, with at least three digits. Project and task-type `prefix` fields do not control these IDs.
- After changing the prefix, run `update-tasks` to normalize existing IDs and internal anchor links. Numeric IDs can still be used with task commands.
- All task commands accept `-f /path/to/tasks.md`; `TASKS_FILE` supplies the default path when exported.

### Command Reference

You can manage tasks using the provided automation scripts in `./scripts/` (or via their aliases):

- **List tasks**:
  - `get-tasks` (or `./scripts/get-tasks`): Show active pending tasks.
  - `get-planning-tasks` (or `get-tasks --planning`): Show tasks in _Planning_ or _Triage_ status.
  - `get-tasks --all`: List all tasks regardless of status.
  - `get-tasks --accept "Status:In Progress"` / `get-tasks --reject "Project:Example"`: Filter tasks.
  - `get-tasks --all --accept "Epic:poc" --select "ID,Title,Epic"`: Filter or select the Epic column. Epic filters accept frontmatter values (`poc`) or labels (`Proof of Concept`), case-insensitively.
  - `get-tasks --all --reject "Epic:poc"`: Exclude an Epic by value or label; comma-separated lists such as `Epic:poc,bootstrap` also work.
- **View a specific task**:
  - `get-task OT-001` (or `./scripts/get-task 1`): Inspect task details, requirements, and metadata.
  - `get-task OT-001 --json`: Output task data in JSON format, including `epic` (value) and `epic_label`.
  - `get-task OT-001 --epic`: Output only the canonical Epic value.
- **Add a new task**:
  - `add-task "Task Title" --project=example-project --type=feature --status=triage`
  - (Optionally supply `-d "Description and checklist"`)
  - Add `--epic=poc` (or `--epic="Proof of Concept"`) to assign an Epic defined in frontmatter.
- **Update an existing task**:
  - `update-task OT-001 --status in_progress`
  - `update-task OT-001 --title "New Title"`
  - `update-task OT-001 --status done --check-all`
  - `update-task OT-001 --append-description "- [ ] Additional subtask"`
  - `update-task OT-001 --epic=poc` / `update-task OT-001 --clear-epic`: Assign or remove an Epic.
- **Synchronize document**:
  - `update-tasks` (or `./scripts/update-tasks`): Re-indexes task IDs, re-renders the summary progress table, and regenerates metadata enum tables.

### Workflow Guidelines

1. **Do Not Edit the Summary Table Manually**: The summary table below is automatically regenerated from the detailed task entries. Use `./scripts/add-task` and `./scripts/update-task`, or edit the detailed task blocks directly and run `./scripts/update-tasks`.
2. **Anchor Tags as SSOT**: Each task in `## Detailed Tasks` is defined by an anchor tag:
   `<a id="ot-XXX" class="task" data-project="PROJECT" data-epic="EPIC" data-status="STATUS" data-task-type="TYPE"></a>`
   The attributes on this anchor tag are the canonical source of truth for the task's state.
   `data-epic` is optional; its value comes from frontmatter `epics`. Summary and detail views display the corresponding label.
3. **Task Lifecycle**:
   - **Planning**: Conceptualization and scoping phase.
   - **Triage**: Requirements known, pending prioritization or design.
   - **Pending**: Ready to be picked up for implementation.
   - **In Progress**: Actively being worked on.
   - **Fixed / Done**: Completed and verified.
   - **Blocked**: Waiting on external dependencies.
   - **Cancelled**: Abandoned or obsolete.
   - **Researching**: Requires investigation before planning.

<a id="tasks-summary"></a>

## Overall Progress

<a id="tasks-list"></a>

| ID     | Title                                 | Project    | Epic                            | Status | Type               |
| :----- | :------------------------------------ | :--------- | :------------------------------ | :----- | :----------------- |
| OT-001 | Proof of Concept                      | Open Tasks |                                 | Fixed  | [Feature](#ot-001) |
| OT-002 | Distribution and Release System       | Open Tasks |                                 | Fixed  | [Feature](#ot-002) |
| OT-003 | Self Hosting and Bootstrap            | Open Tasks |                                 | Fixed  | [Feature](#ot-003) |
| OT-004 | Define WorkItem Metadata              | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-004) |
| OT-005 | Define Comment Format                 | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-005) |
| OT-006 | Define Relationship Format            | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-006) |
| OT-007 | Produce Example WorkItem Documents    | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-007) |
| OT-008 | Implement Project Discovery           | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-008) |
| OT-009 | Implement Git Discovery               | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-009) |
| OT-010 | Implement No-VCS Discovery            | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-010) |
| OT-011 | Implement Configuration Loader        | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-011) |
| OT-012 | Implement Configuration Resolution    | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-012) |
| OT-013 | Implement Protected Key Validation    | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-013) |
| OT-014 | Implement UUID Generation             | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-014) |
| OT-015 | Implement Short Identifier Generation | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-015) |
| OT-016 | Implement Identifier Resolution       | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-016) |
| OT-017 | Implement WorkItem Reader             | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-017) |
| OT-018 | Implement WorkItem Writer             | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-018) |
| OT-019 | Preserve Unknown Content              | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-019) |
| OT-020 | Implement Repository Scanner          | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-020) |
| OT-021 | Implement WorkItem Index              | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-021) |
| OT-022 | Implement Task Listing                | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-022) |
| OT-023 | Implement Task Display                | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-023) |
| OT-024 | Implement Task Creation               | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-024) |
| OT-025 | Implement Task Editing                | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-025) |
| OT-026 | Implement Comment Creation            | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-026) |
| OT-027 | Implement Dependency Management       | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-027) |
| OT-028 | Implement Validation Framework        | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-028) |
| OT-029 | Implement Error Reporting             | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-029) |
| OT-030 | Implement Repair Framework            | Open Tasks | Proof of Concept                | Fixed  | [Feature](#ot-030) |
| OT-031 | Generate Initial Templates            | Open Tasks | Proof of Concept                | Fixed  | [Chore](#ot-031)   |
| OT-032 | Design Release Artifact               | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-032) |
| OT-033 | Build Packaging System                | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-033) |
| OT-034 | Build Global Launcher                 | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-034) |
| OT-035 | Implement Version Discovery           | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-035) |
| OT-036 | Implement Version Validation          | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-036) |
| OT-037 | Implement ot init                     | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-037) |
| OT-038 | Implement Project Installation        | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-038) |
| OT-039 | Implement Version Downloads           | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-039) |
| OT-040 | Implement Transactional Upgrades      | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-040) |
| OT-041 | Implement ot upgrade                  | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-041) |
| OT-042 | Build Cache Management                | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-042) |
| OT-043 | Implement Download Verification       | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-043) |
| OT-044 | Build Release Pipeline                | Open Tasks | Distribution and Release System | Fixed  | [Feature](#ot-044) |
| OT-045 | Initialize Using Open Tasks           | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-045) |
| OT-046 | Create WorkItem Templates             | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-046) |
| OT-047 | Create Meeting Templates              | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-047) |
| OT-048 | Create Initial Backlog                | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-048) |
| OT-049 | Migrate Existing Tasks                | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-049) |
| OT-050 | Validate Migrated Tasks               | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-050) |
| OT-051 | Begin Creating Tasks Using Open Tasks | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-051) |
| OT-052 | Begin Updating Tasks Using Open Tasks | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-052) |
| OT-053 | Retire Legacy Scripts                 | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-053) |
| OT-054 | Archive Legacy Tracker                | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-054) |
| OT-055 | Run First Grooming Meeting            | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-055) |
| OT-056 | Record First Meeting Notes            | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-056) |
| OT-057 | Plan First Release                    | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-057) |
| OT-058 | Verify Development Workflow           | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-058) |
| OT-059 | Declare Bootstrap Complete            | Open Tasks | Self Hosting and Bootstrap      | Fixed  | [Feature](#ot-059) |

---

<a id="task-details"></a>

## Detailed Tasks

<a id="ot-001" class="task" data-project="open-tasks" data-status="done" data-task-type="feature"></a>

### Proof of Concept

**ID:** OT-001
**Project:** Open Tasks
**Status:** Fixed
**Type:** Feature

**Description:**
Validate the core architecture and prove that Open Tasks can manage repository-native WorkItems.

**Requirements:**

- [ ] Define WorkItem format
- [ ] Create WorkItem persistence
- [ ] Create WorkItem commands
- [ ] Build validation system
- [ ] Track work using Open Tasks

<a id="ot-002" class="task" data-project="open-tasks" data-status="done" data-task-type="feature"></a>

### Distribution and Release System

**ID:** OT-002
**Project:** Open Tasks
**Status:** Fixed
**Type:** Feature

**Description:**
Enable installation, packaging, upgrades, and project version management.

**Requirements:**

- [ ] Release artifacts
- [ ] Packaging
- [ ] Launcher
- [ ] Downloads
- [ ] Upgrades

<a id="ot-003" class="task" data-project="open-tasks" data-status="done" data-task-type="feature"></a>

### Self Hosting and Bootstrap

**ID:** OT-003
**Project:** Open Tasks
**Status:** Fixed
**Type:** Feature

**Description:**
Migrate development onto Open Tasks and retire the legacy tracker.

**Requirements:**

- [x] Migrate existing tasks
- [x] Use Open Tasks for Open Tasks
- [x] Retire legacy workflow

<a id="ot-004" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Define WorkItem Metadata

**ID:** OT-004
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Define canonical WorkItem metadata model and YAML frontmatter schema (id, title, type, status, size, created_at, updated_at, author, parent, dependencies, tags, custom fields). Implemented in src/ot/models.py and tested in tests/test_models.py.

<a id="ot-005" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Define Comment Format

**ID:** OT-005
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Define Comment format and markdown rendering (Author, timestamp, unique comment ID, body). Implemented in src/ot/models.py and tested in tests/test_models.py.

<a id="ot-006" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Define Relationship Format

**ID:** OT-006
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Define WorkItem relationship formats (Parent, Child, Depends-on, Blocks) and manipulation APIs. Implemented in src/ot/models.py and tested in tests/test_models.py.

<a id="ot-007" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Produce Example WorkItem Documents

**ID:** OT-007
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Produce example WorkItem documents in examples/sample-project/.ot/tasks/ illustrating Epics, child Features, Bugs with dependencies and comments, and Chores. Tested in tests/test_examples.py.

<a id="ot-008" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Project Discovery

**ID:** OT-008
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement project root discovery by directory tree traversal, environment variable overrides, and fallback resolution. Implemented in src/ot/discovery.py and tested in tests/test_discovery.py.

<a id="ot-009" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Git Discovery

**ID:** OT-009
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Git discovery: git root detection, querying git config for user name, email, and core.editor. Implemented in src/ot/discovery.py and tested in tests/test_discovery.py.

<a id="ot-010" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement No-VCS Discovery

**ID:** OT-010
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement No-VCS discovery and fallbacks for environments without Git or Mercurial, resolving system username, email, and platform default editor. Implemented in src/ot/discovery.py and tested in tests/test_discovery.py.

<a id="ot-011" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Configuration Loader

**ID:** OT-011
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Configuration Loader for reading and parsing JSON configuration files (.ot/config.json, .ot/config.local.json, ~/.ot/config.json). Implemented in src/ot/config.py and tested in tests/test_config.py.

<a id="ot-012" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Configuration Resolution

**ID:** OT-012
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Configuration Resolution layer merging with precedence rules (local > project > global > vcs > env > defaults) and dot-path lookup. Implemented in src/ot/config.py and tested in tests/test_config.py.

<a id="ot-013" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Protected Key Validation

**ID:** OT-013
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Protected Key Validation to detect and warn against improper local overrides of shared project configuration (types, statuses, sizes, meeting types). Implemented in src/ot/config.py and tested in tests/test_config.py.

<a id="ot-014" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement UUID Generation

**ID:** OT-014
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement UUID Generation (RFC 4122 v4 canonical lowercase string generation and validation). Implemented in src/ot/identifiers.py and tested in tests/test_identifiers.py.

<a id="ot-015" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Short Identifier Generation

**ID:** OT-015
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Git-style Short Identifier Generation with adaptive prefix expansion to guarantee repository-wide uniqueness. Implemented in src/ot/identifiers.py and tested in tests/test_identifiers.py.

<a id="ot-016" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Identifier Resolution

**ID:** OT-016
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Identifier Resolution for exact UUID, short unique prefix, and unique title matches, raising explicit AmbiguousIdentifierError or IdentifierNotFoundError when required. Implemented in src/ot/identifiers.py and tested in tests/test_identifiers.py.

<a id="ot-017" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement WorkItem Reader

**ID:** OT-017
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement WorkItem Reader to load and parse markdown files with YAML frontmatter, headers, markdown bodies, and comments. Implemented in src/ot/parser.py and tested in tests/test_parser.py.

<a id="ot-018" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement WorkItem Writer

**ID:** OT-018
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement WorkItem Writer for atomic serialization of WorkItems to disk with formatted YAML frontmatter, markdown sections, and comments. Implemented in src/ot/parser.py and tested in tests/test_parser.py.

<a id="ot-019" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Preserve Unknown Content

**ID:** OT-019
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Preserve unknown user-defined markdown sections, frontmatter fields, and custom content without destructive reformatting during parse-and-write cycles. Implemented in src/ot/parser.py and tested in tests/test_parser.py.

<a id="ot-020" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Repository Scanner

**ID:** OT-020
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Repository Scanner to discover and load all WorkItem markdown documents in the .ot/tasks/ directory hierarchy. Implemented in src/ot/scanner.py and tested in tests/test_scanner.py.

<a id="ot-021" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement WorkItem Index

**ID:** OT-021
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement WorkItem Index for fast query by UUID, unique short prefix, title, parent/child hierarchy traversal, and dependency graph navigation. Implemented in src/ot/scanner.py and tested in tests/test_scanner.py.

<a id="ot-022" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Task Listing

**ID:** OT-022
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot task list' with options for filtering by status, type, size, tag, author, and --json output. Implemented in src/ot/cli.py and tested in tests/test_cli.py.

<a id="ot-023" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Task Display

**ID:** OT-023
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot task show' to display complete WorkItem metadata, parent, children, dependencies, blockers, description, and comments. Implemented in src/ot/cli.py and tested in tests/test_cli.py.

<a id="ot-024" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Task Creation

**ID:** OT-024
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot task create' with CLI flags (--title, --type, --status, --size, --parent, --overview, --no-edit, --edit) and directory structure generation. Implemented in src/ot/cli.py and tested in tests/test_cli.py.

<a id="ot-025" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Task Editing

**ID:** OT-025
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot task edit' (interactive external editor with validation on save) and 'ot task status' for direct status updates. Implemented in src/ot/cli.py and tested in tests/test_cli.py.

<a id="ot-026" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Comment Creation

**ID:** OT-026
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot task comment' with interactive and message argument workflows, timestamping, user author attribution, and markdown persistence. Implemented in src/ot/cli.py and tested in tests/test_cli.py.

<a id="ot-027" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Dependency Management

**ID:** OT-027
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement dependency commands ('ot task add-dependency', 'ot task remove-dependency', 'ot task get-dependencies') with circular/self dependency guards and bidirectional relationship rendering. Implemented in src/ot/cli.py and tested in tests/test_cli.py.

<a id="ot-028" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Validation Framework

**ID:** OT-028
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Validation Framework checking project directories, configuration schemas, UUID validity/uniqueness, work item types/statuses/sizes, broken parent/dependency references, and merge conflict markers. Implemented in src/ot/validation.py and tested in tests/test_validation.py.

<a id="ot-029" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Error Reporting

**ID:** OT-029
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement structured diagnostic error reporting with Severity (ERROR, WARNING, INFO), categories, fixability indicators, formatted console output, and --json output. Implemented in src/ot/validation.py, src/ot/cli.py, and tested in tests/test_validation.py.

<a id="ot-030" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="poc"></a>

### Implement Repair Framework

**ID:** OT-030
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Repair Framework for 'ot check --fix' to safely and automatically repair missing directories, misplaced protected configuration keys, and self-dependencies. Implemented in src/ot/validation.py and tested in tests/test_validation.py.

<a id="ot-031" class="task" data-project="open-tasks" data-status="done" data-task-type="chore" data-epic="poc"></a>

### Generate Initial Templates

**ID:** OT-031
**Project:** Open Tasks
**Epic:** Proof of Concept
**Status:** Fixed
**Type:** Chore

**Description:**
Generate initial template files in .ot/templates/ (tasks/default.md, bug.md, feature.md, epic.md, chore.md, spike.md, meetings/grooming.md, planning.md, retrospective.md, ideation.md, shared/comment.md) and implement template installation system. Implemented in src/ot/templates.py and tested in tests/test_templates.py.

<a id="ot-032" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Design Release Artifact

**ID:** OT-032
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Design Release Artifact format using standalone Python ZipApp (.zipapp) packaging with embedded **main**.py, ReleaseManifest schema, and SHA-256 integrity verification. Implemented in src/ot/packaging.py and tested in tests/test_packaging.py.

<a id="ot-033" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Build Packaging System

**ID:** OT-033
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Build packaging system and release generator in scripts/package-release and ot.packaging for building reproducible self-contained zipapp distributions with checksum manifests. Tested in tests/test_packaging.py.

<a id="ot-034" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Build Global Launcher

**ID:** OT-034
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Build Global Launcher in src/ot/launcher.py with project root resolution, configured version discovery, and delegation to project-installed binary (.ot/bin/ot.zipapp). Tested in tests/test_launcher.py.

<a id="ot-035" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement Version Discovery

**ID:** OT-035
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Version Discovery to inspect project configured version (.ot/config.json) and installed binary metadata (.ot/bin/ot-manifest.json). Implemented in src/ot/version.py and tested in tests/test_packaging.py.

<a id="ot-036" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement Version Validation

**ID:** OT-036
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Version Validation for checking semantic version conformance and detecting mismatches between configured and installed tool versions. Integrated into Validator (ot check) and tested in tests/test_packaging.py.

<a id="ot-037" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement ot init

**ID:** OT-037
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot init' command for initializing new Open Tasks projects with directory structure, system.toolVersion, project configuration, and default templates. Implemented in src/ot/installation.py, src/ot/cli.py, and tested in tests/test_installation.py.

<a id="ot-038" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement Project Installation

**ID:** OT-038
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Project Installation mechanism to install versioned executable zipapp, manifest, and optional root wrapper scripts (otw, otw.bat) in .ot/bin/. Implemented in src/ot/installation.py and tested in tests/test_installation.py.

<a id="ot-039" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement Version Downloads

**ID:** OT-039
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Version Downloads for fetching, caching, and staging release zipapps and manifests from mirrors or release builds. Implemented in src/ot/upgrade.py and tested in tests/test_upgrade.py.

<a id="ot-040" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement Transactional Upgrades

**ID:** OT-040
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Transactional Upgrades with isolated temporary staging, semver downgrade prevention, non-destructive template preservation, validation checks, and atomic commit on success. Implemented in src/ot/upgrade.py and tested in tests/test_upgrade.py.

<a id="ot-041" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement ot upgrade

**ID:** OT-041
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement 'ot upgrade' CLI command supporting --version <v>, --mirror <dir>, and --dry-run flags for automated project upgrades. Implemented in src/ot/cli.py, src/ot/upgrade.py, and tested in tests/test_upgrade.py.

<a id="ot-042" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Build Cache Management

**ID:** OT-042
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Build global cache management in ~/.ot/cache/ and ~/.ot/versions/ for local caching of downloaded zipapps, manifests, and artifacts. Implemented in src/ot/cache.py and tested in tests/test_upgrade.py.

<a id="ot-043" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Implement Download Verification

**ID:** OT-043
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Implement Download Verification using cryptographic SHA-256 validation to prevent corrupted or tampered downloads from being unpacked or executed. Implemented in src/ot/cache.py and tested in tests/test_upgrade.py.

<a id="ot-044" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="distribution"></a>

### Build Release Pipeline

**ID:** OT-044
**Project:** Open Tasks
**Epic:** Distribution and Release System
**Status:** Fixed
**Type:** Feature

**Description:**
Build automated release pipeline script in scripts/build-release executing test suite, zipapp packaging, manifest creation, SHA256 checksum generation, and post-build verification.

<a id="ot-045" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Initialize Using Open Tasks

**ID:** OT-045
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Initialize self-hosted Open Tasks repository structure (.ot/, config.json, templates/, bin/, otw, otw.bat) in the repository root. Verified with 'otw version' and 'otw check'.

<a id="ot-046" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Create WorkItem Templates

**ID:** OT-046
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Created and validated WorkItem templates in .ot/templates/tasks/ (feature.md, bug.md, epic.md, chore.md, spike.md, default.md) with YAML frontmatter placeholders and markdown sections.

<a id="ot-047" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Create Meeting Templates

**ID:** OT-047
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Created and validated meeting templates in .ot/templates/meetings/ (grooming.md, planning.md, retrospective.md, ideation.md) with agenda, discussion, decisions, and action item sections.

<a id="ot-048" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Create Initial Backlog

**ID:** OT-048
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Created initial repository-native backlog in .ot/tasks/ with epics and features ('Export and Reporting Tooling', 'Mercurial VCS Integration', 'JSON Schema Export'). Verified with 'otw task list' and 'otw check'.

<a id="ot-049" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Migrate Existing Tasks

**ID:** OT-049
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Migrated all 59 existing tasks, epics, descriptions, requirements, and metadata from docs/tasks.md into repository-native .ot/tasks/ hierarchy. Verified with 'otw task list' and 'otw check'.

<a id="ot-050" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Validate Migrated Tasks

**ID:** OT-050
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Validated all migrated tasks across the repository using 'otw check' and 'otw check --json'. All YAML frontmatter schemas, UUID uniqueness, relationships, and directory structures verified with 0 errors/warnings.

<a id="ot-051" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Begin Creating Tasks Using Open Tasks

**ID:** OT-051
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Adopted 'otw task create' for creating new repository-native tasks with automated slug directory generation, template instantiation, and parent relationship linking.

<a id="ot-052" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Begin Updating Tasks Using Open Tasks

**ID:** OT-052
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Adopted 'otw task status', 'otw task comment', 'otw task add-dependency', and 'otw task edit' for updating and progressing WorkItems directly in the repository.

<a id="ot-053" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Retire Legacy Scripts

**ID:** OT-053
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Retired legacy Markdown tracker scripts in scripts/ (get-tasks, get-task, add-task, update-task, update-tasks) in favor of the self-hosted Open Tasks CLI (otw / ot). Documented retirement and migration mapping in scripts/README.md.

<a id="ot-054" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Archive Legacy Tracker

**ID:** OT-054
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Archived docs/tasks.md single-file tracker with an archival header notice directing all task management workflows to repository-native .ot/tasks/ and the otw CLI.

<a id="ot-055" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Run First Grooming Meeting

**ID:** OT-055
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Conducted first repository-native backlog grooming meeting reviewing migrated backlog items and planning first release.

<a id="ot-056" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Record First Meeting Notes

**ID:** OT-056
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Recorded first meeting notes in .ot/meetings/2026-10-02-grooming.md adhering to ADR-0021 repository-based meeting notes and review workflow.

<a id="ot-057" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Plan First Release

**ID:** OT-057
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Planned initial v0.1.0 release. Created release tracking task 800d17 (Release v0.1.0) under Distribution and Release System epic and documented release plan in .ot/meetings/2026-10-02-release-0.1.0-plan.md.

<a id="ot-058" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Verify Development Workflow

**ID:** OT-058
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Verified complete end-to-end development workflow in self-hosted repository: otw version, otw check, otw task queries, release packaging, and unit tests passing with zero errors.

<a id="ot-059" class="task" data-project="open-tasks" data-status="done" data-task-type="feature" data-epic="bootstrap"></a>

### Declare Bootstrap Complete

**ID:** OT-059
**Project:** Open Tasks
**Epic:** Self Hosting and Bootstrap
**Status:** Fixed
**Type:** Feature

**Description:**
Declared Self Hosting and Bootstrap (Phase 3) complete! Open Tasks is fully operational, self-hosted, and managing its own development lifecycle.

---

## Notes

- This file uses monotonic identifiers with a configurable prefix and at least three digits (e.g. `OT-001`, `OT-002`).
- Run `./scripts/update-tasks` whenever manually editing tasks to keep all tables synchronized.

#### Task System Documentation (Requirements for Agents)

- **Single Source of Truth (SSOT)**:
  - The `id` attribute on the anchor tag is the SSOT for the Task ID.
  - The `data-status` attribute on the anchor tag is the SSOT for the Status value.
  - The `data-task-type` attribute on the anchor tag is the SSOT for the Type value.
  - The optional `data-epic` attribute is the SSOT for the Epic value; labels come from frontmatter `epics`.
- **Detailed Task Identification**: Any anchor tag with the `task` class identifies the start of a task details section.
- **Rendered Summary Views**:
  - The **Overall Progress Table** is a rendered summary of task data. It must be updated whenever the SSOT attributes are modified.
  - The **Status and Type Descriptions** sections at the end of the doc are rendered versions of the YAML frontmatter (task-statuses and task-types respectively).
- **ID Formatting**: All IDs follow the configured `PREFIX-XXX` format where `XXX` is a monotonic number padded to at least three digits.
- **Task Lifecycle**:
  1. **Planning**: The task is being scoped and conceptualized. We still don't know what we want.
  2. **Triage**: Requirements are identified, but we don't know how we want to do it.
  3. **Pending**: Information complete, ready for implementation.
  4. **In Progress**: Work active.
  5. **Fixed / Done**: Work completed.
  6. **Blocked**: Work stopped by external dependency.
  7. **Cancelled**: Task discarded.

#### Projects (Rendered from frontmatter projects)

| Value      | Label      | Prefix | Path |
| :--------- | :--------- | :----- | :--- |
| open-tasks | Open Tasks | OT     | .    |

#### Task Statuses (Rendered from frontmatter task-statuses)

| Value       | Label       | Description                                                                      |
| :---------- | :---------- | :------------------------------------------------------------------------------- |
| planning    | Planning    | The task is being scoped and conceptualized. We still don't know what we want.   |
| triage      | Triage      | The task is being evaluated and prioritized. We don't know how we want to do it. |
| pending     | Pending     | The task is ready to be acted on.                                                |
| in_progress | In Progress | The task is currently being worked on.                                           |
| done        | Fixed       | The task has been completed.                                                     |
| blocked     | Blocked     | The task cannot proceed due to an obstacle or dependency.                        |
| cancelled   | Cancelled   | The task was decided against or is no longer relevant.                           |
| research    | Researching | This task needs more research before planning.                                   |

#### Task Types (Rendered from frontmatter task-types)

| Value   | Label   | Prefix | Description                                                |
| :------ | :------ | :----- | :--------------------------------------------------------- |
| lint    | Lint    | LNT    | The task involves fixing a linting error or other warning. |
| bug     | Bug     | BUG    | The task is a bug to fix.                                  |
| feature | Feature | ENH    | The task is a new feature to implement.                    |
| chore   | Chore   | CHR    | The task is a routine maintenance or administrative task.  |

#### Epics (Rendered from frontmatter epics)

| Value        | Label                           | Description                                                                                  |
| :----------- | :------------------------------ | :------------------------------------------------------------------------------------------- |
| poc          | Proof of Concept                | Validate the core architecture and WorkItem model.                                           |
| distribution | Distribution and Release System | Enable installation, upgrades, packaging, release workflows, and project version management. |
| bootstrap    | Self Hosting and Bootstrap      | Migrate development onto Open Tasks and retire the legacy tracker.                           |

<!-- Table Sort Injection -->
<!-- @import "assets/table-sort.css" -->
<!-- @import "assets/table-sort.js" -->
<link rel="stylesheet" href="assets/table-sort.css">
<script src="assets/table-sort.js"></script>
