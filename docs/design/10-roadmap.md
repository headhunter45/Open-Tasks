# Roadmap

## Purpose

This document describes the anticipated development direction for Open Tasks (ot).

Unlike ADRs, roadmap items are not commitments.

Items may be:

- Added
- Removed
- Reordered
- Replaced

based on project needs and lessons learned during implementation.

---

# Current Phase

## Phase 0 - Planning

Status:

In Progress

Goals:

- Define core architecture
- Define repository layout
- Define configuration system
- Define WorkItem model
- Define meeting model
- Define upgrade model

Success Criteria:

- ADRs completed
- Core design docs completed
- Open questions documented

---

# Phase 1 - Proof of Concept

Status:

Planned

Goals:

- Basic project initialization
- Basic WorkItem storage
- UUID generation
- Short ID resolution
- Markdown parsing
- WorkItem creation
- WorkItem listing
- WorkItem display

Potential Commands:

```text
ot init
ot task create
ot task list
ot task show
```

Success Criteria:

- Create WorkItems
- Store WorkItems
- Resolve identifiers
- Render task summaries

---

# Phase 2 - Editing Workflows

Status:

Planned

Goals:

- Editor integration
- Task editing
- Comment support
- Status updates
- Relationship management

Potential Commands:

```text
ot task edit
ot task comment
ot task status
ot task add-dependency
ot task remove-dependency
```

Success Criteria:

- End-to-end task lifecycle works

---

# Phase 3 - Validation

Status:

Planned

Goals:

- Relationship validation
- Configuration validation
- Link validation
- Repair operations

Potential Commands:

```text
ot check
ot check --fix
```

Success Criteria:

- Detect common data corruption issues
- Repair safe problems

---

# Phase 4 - Meetings

Status:

Planned

Goals:

- Meeting templates
- Meeting creation
- Meeting completion
- WorkItem integration

Potential Commands:

```text
ot meeting start
ot meeting end
ot meeting list
```

Success Criteria:

- Backlog grooming workflow completed

---

# Phase 5 - Upgrades And Versioning

Status:

Planned

Goals:

- Project-installed versions
- Version discovery
- Upgrade process
- Migration support

Potential Commands:

```text
ot upgrade
ot version
```

Success Criteria:

- Safe upgrades between versions

---

# Future Work

Potential future areas include:

- Sprint support
- Reporting
- Import tooling
- Export tooling
- Attachment management
- Mercurial integration
- Plugin system
- Repository analytics

No commitment has been made to implement these features.

---

# Deferred Items

The following topics are intentionally deferred until the core system is working:

- Web interfaces
- Database backends
- Hosted services
- Real-time collaboration
- Bidirectional synchronization with external systems

See:

- ADR-0016 No Database Backend
- ADR-0019 Export as a Separate Concern
