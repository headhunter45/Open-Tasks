---
name: task-management
description: >-
  Manage, query, create, triage, inspect, and update project tasks using Open Tasks
  (ot / ./otw). Activate this skill whenever reading, creating, editing, prioritizing,
  or updating tasks, checklists, or project progress.
---

# Task Management Skill

This skill provides operational guidelines and procedures for managing project tasks using **Open Tasks (`ot` / `./otw`)**. All tasks, epics, bugs, and meeting records are stored directly in the repository under `.ot/tasks/` and `.ot/meetings/`.

---

## Quick Reference

In the repository root, run commands through the self-hosted wrapper `./otw` (or the global `ot` CLI):

```bash
# Verify project version and health
./otw version
./otw check
```

---

## Core Procedures

### 1. Querying and Inspecting Tasks

- **List active work items**:
  ```bash
  ./otw task list
  ```
- **Filter by status**:
  ```bash
  ./otw task list --status planned
  ./otw task list --status in_progress
  ./otw task list --status completed
  ./otw task list --status blocked
  ```
- **Filter by type**:
  ```bash
  ./otw task list --type epic
  ./otw task list --type feature
  ./otw task list --type bug
  ./otw task list --type chore
  ```
- **Inspect a specific task** (by 6-char short ID, UUID, or title):
  ```bash
  ./otw task show 075920
  ./otw task show "Cleanup source tree."
  ```

---

### 2. Creating WorkItems

Create new tasks using template instantiation:

```bash
./otw task create \
  --title "Implement Cache Invalidation" \
  --type feature \
  --status planned \
  --size medium \
  --parent "Distribution and Release System" \
  --overview "Support explicit cache invalidation in ot upgrade." \
  --no-edit
```

Available types: `feature`, `bug`, `task`, `chore`, `spike`, `epic`.
Available statuses: `triage`, `planned`, `in_progress`, `blocked`, `completed`, `closed`.
Available sizes: `small`, `medium`, `large`.

---

### 3. Updating Lifecycles & Recording Progress

- **Update Task Status**:
  ```bash
  ./otw task status "Implement Cache Invalidation" in_progress
  ./otw task status "Implement Cache Invalidation" completed
  ```
- **Append Timestamped Comment**:
  ```bash
  ./otw task comment "Implement Cache Invalidation" "Implemented cache clearing on version mismatch."
  ```
- **Add Task Dependency / Blocker**:
  ```bash
  ./otw task add-dependency "Implement Cache Invalidation" "Build Cache Management"
  ```

---

### 4. Integrity Validation & Automatic Repair

Run diagnostic checks before concluding tasks or submitting PRs:

```bash
# Check repository integrity (UUID uniqueness, relationships, schema validity)
./otw check

# Output diagnostics as JSON
./otw check --json

# Automatically repair trivial inconsistencies
./otw check --fix
```
