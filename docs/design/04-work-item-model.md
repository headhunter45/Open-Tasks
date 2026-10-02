# Work Item Model

## Overview

This document describes the WorkItem model used by Open Tasks (ot).

A WorkItem is the primary planning object in OT.

Examples include:

- Tasks
- Bugs
- Enhancements
- Epics
- Spikes
- Chores
- Future planning object types

OT uses a unified WorkItem model rather than separate task and epic models.

See:

- ADR-0003 Unified WorkItem Model

---

# Goals

The WorkItem model should support:

- Arbitrary nesting
- Flexible planning structures
- Repository-native storage
- Human-readable data
- Direct editing
- Hierarchical planning
- Dependency management

The model should not impose a specific planning methodology on projects.

---

# Work Item Definition

A WorkItem represents a unit of work, planning, investigation, coordination, or delivery.

Examples:

```text
Release
Feature
Epic
Task
Bug
Enhancement
Spike
Chore
```

The distinction between these concepts is expressed through metadata rather than separate model implementations.

---

# Work Item Types

Each WorkItem has a type.

Examples:

```text
epic
task
bug
enhancement
spike
chore
```

Projects may define additional types.

Valid types are configured through:

```text
workItem.types
```

See:

- 03-configuration-system.md

---

# Hierarchy

WorkItems may contain child WorkItems.

Example:

```text
Version 3.0 Release
└─ User Authentication
   ├─ Login Workflow
   ├─ Password Reset
   └─ Account Recovery
```

The hierarchy allows teams to model work at multiple levels.

Examples:

```text
Release
  Epic
    Feature
      Task
```

or

```text
Epic
  Task
    Subtask
```

OT intentionally does not enforce a fixed hierarchy.

---

# Parent Relationships

A WorkItem may have:

```text
0 or 1 parent WorkItem
```

Top-level WorkItems have no parent.

Examples:

```text
Release
```

or

```text
Backlog Item
```

---

# Child Relationships

A WorkItem may have:

```text
0..N children
```

Children represent decomposition of work.

Examples:

- Subtasks
- Features
- Epics
- Deliverables

The meaning of the relationship is determined by project conventions rather than OT.

---

# Dependency Relationships

WorkItems may have dependency relationships independent of hierarchy.

Example:

```text
Task A
depends on
Task B
```

or

```text
Bug Fix
depends on
Migration Completion
```

Dependency relationships represent ordering requirements.

---

# Relationship Types

Current relationship categories:

```text
Parent
Child

Dependency Parent
Dependency Child
```

Additional relationship types may be added in the future.

See:

- OQ-0009 Work Item Relationship Representation

---

# Canonical Identifier

Every WorkItem possesses a UUID.

Example:

```text
550e8400-e29b-41d4-a716-446655440000
```

The UUID is the canonical identifier for the WorkItem.

UUIDs are intended for:

- Internal references
- Storage
- Data integrity

See:

- ADR-0007 UUID Backed Identifiers

---

# Short Identifiers

Users primarily interact with WorkItems through short identifiers.

Example:

```text
4f2a9c
```

Short identifiers provide a Git-like user experience.

OT should:

- Display unique prefixes
- Accept unambiguous prefixes
- Expand identifiers when ambiguity exists

The exact implementation remains under discussion.

See:

- ADR-0008 Git Style Short Identifiers
- OQ-0008 Work Item Short Identifier Implementation

---

# Titles

Each WorkItem has a title.

Example:

```text
Main Menu Background Should Be Red
```

Titles are intended to be:

- Human readable
- Descriptive
- Searchable

Titles are not identifiers.

Multiple WorkItems may have identical titles.

---

# Status

Every WorkItem possesses a status.

Valid statuses are defined by the project.

Example statuses:

```text
triage
planned
in_progress
blocked
completed
closed
```

Status values are configured through:

```text
workItem.statuses
```

---

# Size

WorkItems may be assigned a size value.

Examples:

```text
small
medium
large
extra_large
```

Projects define their own sizing systems.

Valid sizes are configured through:

```text
workItem.sizes
```

---

# Overview

Each WorkItem may contain an overview section.

Purpose:

- Summary
- Requirements
- Context
- Goals

The overview is intended to provide a concise description of the WorkItem.

---

# Description

Each WorkItem may contain long-form descriptive content.

Examples:

- Requirements
- Notes
- Design information
- Investigation results

Description content is primarily human-readable.

---

# Comments

WorkItems support comments.

Comments represent historical discussion and updates.

Example information:

```text
Author
Timestamp
Comment Body
```

Comments are intended to behave similarly to issue-tracker comments.

---

# Attachments

WorkItems may reference attachments.

Examples:

```text
Images
Documents
Diagrams
Spreadsheets
External URLs
```

Attachments may be:

```text
Repository-local
External references
```

Attachment ownership rules remain under discussion.

See:

- OQ-0002 Attachment Identifier Strategy
- OQ-0003 Attachment Metadata Model
- OQ-0017 Attachment Ownership Rules

---

# Metadata

WorkItems contain machine-readable metadata.

Examples:

```text
UUID
Type
Status
Size
Relationships
Creation Date
Modification Date
```

Metadata is used for:

- Validation
- Filtering
- Reporting
- Navigation

---

# Direct Editing

WorkItem files are intended to be edited directly by users.

Users may:

- Edit manually
- Use ot commands
- Use external editors

OT validates content rather than preventing manual modification.

See:

- ADR-0027 Direct File Editing Is Supported

---

# Validation

The following should be validated:

- UUID presence
- Valid type
- Valid status
- Valid size
- Relationship integrity
- Attachment integrity
- Reference integrity

Validation is provided through:

```text
ot check
ot check --fix
```

See:

- ADR-0023 First Class Validation And Repair

---

# Unknown Content

Not all content within a WorkItem must be recognized by OT.

Example:

```markdown
## Investigation Notes

Some manually written notes...
```

Content without expected OT metadata may be treated as normal Markdown.

OT should preserve unknown content whenever possible.

---

# Work Item Discovery

A document is recognized as a WorkItem when required metadata is present.

The exact recognition mechanism remains to be finalized.

Current expectation:

WorkItems are identified through UUID-based metadata.

Content lacking required metadata is treated as ordinary Markdown content.

---

# Movement And Refactoring

WorkItems may be:

- Renamed
- Moved
- Re-parented

Because identifiers are UUID-based, these operations should not affect references.

This allows projects to reorganize planning structures without breaking relationships.

---

# Reporting

Because metadata is structured, WorkItems may be filtered and reported by:

- Type
- Status
- Size
- Parent
- Child
- Dependency
- Author
- Attachment

Examples:

```text
ot task list --status blocked

ot task list --type bug

ot task list --size large
```

---

# Open Questions

The following topics remain unresolved:

- OQ-0001 Final Work Item Filesystem Layout
- OQ-0002 Attachment Identifier Strategy
- OQ-0003 Attachment Metadata Model
- OQ-0008 Work Item Short Identifier Implementation
- OQ-0009 Work Item Relationship Representation
- OQ-0012 Work Item Display Naming
- OQ-0017 Attachment Ownership Rules
