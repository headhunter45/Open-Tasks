# Open Tasks (ot)

Open Tasks is a repository-native, database-free task and planning management tool designed for modern development workflows.

---

## Key Features

- **Repository-Native Storage**: All tasks, bugs, epics, and meeting notes are stored as Markdown documents with YAML frontmatter in `.ot/tasks/`.
- **Database-Free**: Everything is persisted directly in Git or your local filesystem.
- **UUID & Git-Style Short Identifiers**: Stable UUID-backed internal references with convenient, unambiguous short prefix identifiers for human interaction.
- **Direct File Editing**: Seamless round-trip editing via text editors or the CLI without loss of custom user sections.
- **Dependency & Hierarchy Graphs**: Unified WorkItem model supporting arbitrary parent/child nesting and bidirectional blocker/dependency tracking.
- **First-Class Validation & Repair**: `ot check` and `ot check --fix` for automatic detection and repair of configuration and filesystem inconsistencies.

---

## Quick Start

### Running Unit Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

### Trying the CLI

```bash
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"

# List work items in the sample project
python3 -m ot.cli -C examples/sample-project task list

# Show detailed work item information
python3 -m ot.cli -C examples/sample-project task show "Release Alpha"

# Check project health
python3 -m ot.cli -C examples/sample-project check
```

---

## Documentation

- [Phase 1 Testing and Verification Guide (Core Engine)](docs/phase-1-testing-and-verification.md)
- [Phase 2 Testing and Verification Guide (Distribution & Release)](docs/phase-2-testing-and-verification.md)
- [Phase 3 Testing and Verification Guide (Self-Hosting & Bootstrap)](docs/phase-3-testing-and-verification.md)
- [Architecture & Design Documents](docs/design/)
- [Project Task Tracker (Archived)](docs/tasks.md)
