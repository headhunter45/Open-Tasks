# Glossary

## Purpose

This document defines terminology used throughout the Open Tasks (ot) project.

The glossary exists to ensure that documentation, code, templates, and discussions use consistent language.

When a term is defined here, other documents should prefer that definition.

---

# Work Item

A WorkItem is the primary planning object in OT.

Examples include:

- Tasks
- Bugs
- Enhancements
- Epics
- Spikes
- Chores

All of these are represented using the same underlying model.

See:

- ADR-0003 Unified WorkItem Model
- 04-work-item-model.md

---

# Type

A configurable classification applied to a WorkItem.

Examples:

```text
task
bug
enhancement
epic
spike
chore
```

Projects may define additional types.

Types are metadata and do not correspond to different implementation classes.

---

# Status

A configurable lifecycle state assigned to a WorkItem.

Examples:

```text
triage
planned
in_progress
blocked
completed
closed
```

Status values are project-defined.

---

# Size

A configurable estimate value assigned to a WorkItem.

Examples:

```text
small
medium
large
extra_large
```

Projects may use whatever sizing system best fits their workflow.

---

# Parent

A WorkItem that directly contains another WorkItem.

A WorkItem may have zero or one parent.

---

# Child

A WorkItem directly contained by another WorkItem.

A WorkItem may have zero or more children.

---

# Dependency

A relationship indicating that one WorkItem depends on another.

Dependencies are separate from parent-child relationships.

Example:

```text
Task A depends on Task B
```

---

# Attachment

Content associated with a WorkItem or Meeting.

Examples:

- Images
- Documents
- URLs
- Diagrams
- External resources

Attachment metadata remains an active design area.

---

# Comment

A timestamped entry attached to a WorkItem.

Comments typically include:

- Author
- Timestamp
- Content

Comments provide historical discussion and updates.

---

# Work Item Tree

The hierarchy formed by parent-child relationships.

Example:

```text
Release
└─ Epic
   └─ Task
      └─ Subtask
```

OT does not impose a specific hierarchy structure.

---

# Meeting

A repository artifact that records planning activity and decisions.

Examples:

- Grooming
- Planning
- Retrospective
- Ideation

Meetings produce repository content rather than acting as real-time collaboration sessions.

---

# Meeting Type

A configurable category assigned to a Meeting.

Examples:

```text
grooming
planning
retrospective
ideation
```

Meeting types are project-defined.

---

# Attendee

A participant in a Meeting.

Attendees may be represented by:

- Name
- Email
- Username

Exact representation remains flexible.

---

# Sprint

A planned period of work.

Sprint representation remains an open question.

See:

- OQ-0004 Sprint Representation

---

# Template

A user-editable file used to generate OT content.

Examples:

- WorkItem templates
- Meeting templates
- Comment templates

Templates are stored within the repository.

---

# Repository

The project storage location containing:

- Source code
- OT data
- Templates
- Configuration

The repository is the authoritative source of project information.

---

# Project Root

The root directory of an OT project.

Current discovery priority:

```text
.ot
.git
.hg
Current Directory
```

See:

- ADR-0028 Project Root Discovery

---

# .ot Directory

The canonical OT project directory.

Contains:

- Configuration
- WorkItems
- Meetings
- Templates
- Installed OT implementation

See:

- ADR-0029 .ot Directory As Canonical Tool Root

---

# Launcher

The globally installed OT executable.

Example:

```text
ot
```

Responsibilities include:

- Project discovery
- Version discovery
- Launching the project implementation

The launcher is distinct from the project-installed implementation.

---

# Project Implementation

The versioned OT executable installed within a project.

Example:

```text
.ot/bin/ot.py
```

This executable performs actual project operations.

---

# Wrapper

An optional project-local script used to invoke OT.

Examples:

```text
otw
otw.bat
```

Wrappers are primarily intended for CI and restricted environments.

---

# UUID

The canonical identifier assigned to a WorkItem.

UUIDs are globally unique.

UUIDs are intended for machine use and storage.

---

# Short Identifier

A user-friendly identifier derived from a WorkItem UUID.

Short identifiers are intended to behave similarly to Git short hashes.

Users primarily interact with WorkItems through short identifiers.

---

# Protected Configuration Key

A configuration value that affects shared project behavior.

Examples:

```text
workItem.types
workItem.statuses
workItem.sizes
meeting.types
```

Protected keys should normally be stored in project configuration rather than local overrides.

---

# Validation

The process of detecting inconsistencies within OT project data.

Examples:

- Broken references
- Invalid statuses
- Missing WorkItems
- Invalid configuration

Provided through:

```text
ot check
```

---

# Repair

The process of automatically correcting safe validation issues.

Provided through:

```text
ot check --fix
```

Repairs should be conservative and preserve user data.

---

# Repository-Native

A design philosophy in which project data lives inside the repository and participates in normal version-control workflows.

Repository-native data:

- Can be reviewed
- Can be branched
- Can be merged
- Can be audited

using existing tooling.

---

# Source Of Truth

The authoritative location for a piece of information.

For OT:

```text
Repository Files
```

are the source of truth.

External systems may consume OT data, but the repository remains authoritative.

---

# Pull Request

The preferred review mechanism for OT changes.

Examples:

- WorkItem updates
- Meeting records
- Template modifications
- Configuration changes

OT relies heavily on existing pull-request workflows.

---

# Direct Editing

The act of manually editing OT-managed files without using OT commands.

Direct editing is a supported workflow.

OT favors validation and repair rather than preventing direct modification.

---

# OT

Short for:

```text
Open Tasks
```

Pronounced:

```text
oat
```

OT is a repository-native planning and work tracking system.
