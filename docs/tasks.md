---
projects:
  - label: 'Example Project'
    path: 'src/example'
    prefix: 'EXP'
    value: 'example-project'
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

# Project Task Tracker

This document serves as the Single Source of Truth (SSOT) for tracking tasks, features, bugs, chores, and lint issues across the project.

## Instructions for Working with Tasks

### Quick Start (Environment Setup)
Before running task commands, source the helper environment script in your shell to load convenient aliases and paths:
```bash
source ./scripts/env.sh
```

### Command Reference
You can manage tasks using the provided automation scripts in `./scripts/` (or via their aliases):
- **List tasks**:
  - `get-tasks` (or `./scripts/get-tasks`): Show active pending tasks.
  - `get-planning-tasks` (or `get-tasks --planning`): Show tasks in *Planning* or *Triage* status.
  - `get-tasks --all`: List all tasks regardless of status.
  - `get-tasks --accept "Status:In Progress"` / `get-tasks --reject "Project:Example"`: Filter tasks.
- **View a specific task**:
  - `get-task FGJ-001` (or `./scripts/get-task 1`): Inspect task details, requirements, and metadata.
  - `get-task FGJ-001 --json`: Output task data in JSON format.
- **Add a new task**:
  - `add-task "Task Title" --project=example-project --type=feature --status=triage`
  - (Optionally supply `-d "Description and checklist"`)
- **Update an existing task**:
  - `update-task FGJ-001 --status in_progress`
  - `update-task FGJ-001 --title "New Title"`
  - `update-task FGJ-001 --status done --check-all`
  - `update-task FGJ-001 --append-description "- [ ] Additional subtask"`
- **Synchronize document**:
  - `update-tasks` (or `./scripts/update-tasks`): Re-indexes task IDs, re-renders the summary progress table, and regenerates metadata enum tables.

### Workflow Guidelines
1. **Do Not Edit the Summary Table Manually**: The summary table below is automatically regenerated from the detailed task entries. Use `./scripts/add-task` and `./scripts/update-task`, or edit the detailed task blocks directly and run `./scripts/update-tasks`.
2. **Anchor Tags as SSOT**: Each task in `## Detailed Tasks` is defined by an anchor tag:
   `<a id="fgj-XXX" class="task" data-project="PROJECT" data-status="STATUS" data-task-type="TYPE"></a>`
   The attributes on this anchor tag are the canonical source of truth for the task's state.
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

| ID      | Title                                       | Project         | Status | Type                |
|:------|:------------------------------------------|:--------------|:-----|:------------------|
| FGJ-001 | *Example Task: Initialize Project Template* | Example Project | Triage | [Feature](#fgj-001) |

---

<a id="task-details"></a>

## Detailed Tasks

<a id="fgj-001" class="task" data-project="example-project" data-status="triage" data-task-type="feature"></a>
### Example Task: Initialize Project Template
**ID:** FGJ-001
**Project:** Example Project
**Status:** Triage
**Type:** Feature

**Description:**
This is an example task template demonstrating how task entries are structured and managed. Use `scripts/add-task` to create real tasks for your project.

**Requirements:**
- [ ] Define initial requirements and scope
- [ ] Plan implementation architecture
- [ ] Execute tasks and verify results

---

## Notes

- This file uses monotonic 3-digit identifiers (e.g. `FGJ-001`, `FGJ-002`).
- Run `./scripts/update-tasks` whenever manually editing tasks to keep all tables synchronized.

#### Task System Documentation (Requirements for Agents)

- **Single Source of Truth (SSOT)**:
  - The `id` attribute on the anchor tag is the SSOT for the Task ID.
  - The `data-status` attribute on the anchor tag is the SSOT for the Status value.
  - The `data-task-type` attribute on the anchor tag is the SSOT for the Type value.
- **Detailed Task Identification**: Any anchor tag with the `task` class identifies the start of a task details section.
- **Rendered Summary Views**:
  - The **Overall Progress Table** is a rendered summary of task data. It must be updated whenever the SSOT attributes are modified.
  - The **Status and Type Descriptions** sections at the end of the doc are rendered versions of the YAML frontmatter (task-statuses and task-types respectively).
- **ID Formatting**: All IDs follow the `FGJ-XXX` format where `XXX` is a monotonic 3-digit number.
- **Task Lifecycle**:
  1. **Planning**: The task is being scoped and conceptualized. We still don't know what we want.
  2. **Triage**: Requirements are identified, but we don't know how we want to do it.
  3. **Pending**: Information complete, ready for implementation.
  4. **In Progress**: Work active.
  5. **Fixed / Done**: Work completed.
  6. **Blocked**: Work stopped by external dependency.
  7. **Cancelled**: Task discarded.

#### Projects (Rendered from frontmatter projects)
| Value           | Label           | Prefix | Path        |
|:--------------|:--------------|:-----|:----------|
| example-project | Example Project | EXP    | src/example |

#### Task Statuses (Rendered from frontmatter task-statuses)
| Value       | Label       | Description                                                                      |
|:----------|:----------|:-------------------------------------------------------------------------------|
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
|:------|:------|:-----|:---------------------------------------------------------|
| lint    | Lint    | LNT    | The task involves fixing a linting error or other warning. |
| bug     | Bug     | BUG    | The task is a bug to fix.                                  |
| feature | Feature | ENH    | The task is a new feature to implement.                    |
| chore   | Chore   | CHR    | The task is a routine maintenance or administrative task.  |

<!-- Table Sort Injection -->
<!-- @import "assets/table-sort.css" -->
<!-- @import "assets/table-sort.js" -->
<link rel="stylesheet" href="assets/table-sort.css">
<script src="assets/table-sort.js"></script>
