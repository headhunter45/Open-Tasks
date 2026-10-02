# Design Notes and Alternatives

## Purpose

This document captures design discussions, influencing ideas, rejected approaches, and architectural reasoning that do not fit naturally into ADRs.

The goal of this document is to preserve context and design intent.

Unlike ADRs:

- Contents of this document are not necessarily decisions.
- Topics may remain unresolved.
- Ideas may be revisited later.

This document exists primarily to preserve institutional memory.

---

# Naming History

## Original Concept

OT began as an exploration of treating planning and task management similarly to source control.

An early joke description was:

```text
Git For Tasks
```

This produced the joke command name:

```text
tit
```

where:

```text
git
```

became:

```text
tit
```

for:

```text
Tasks In Tracking
```

or simply:

```text
Git For Tasks
```

This was intentionally not adopted.

Reasons:

- Poor professionalism
- Unwanted interpretations
- Unsuitable for workplaces
- Difficult to recommend to organizations

---

## Open Tasks

The eventual choice was:

```text
Open Tasks
```

with the command:

```text
ot
```

pronounced:

```text
oat
```

Reasons:

- Short
- Easy to type
- Easy to remember
- Acceptable in professional environments
- Unlikely to conflict with existing tools

---

# Major Influences

## Git

Git strongly influenced OT.

Examples include:

- Repository-native storage
- Pull request workflows
- Branch-based planning
- Short identifier concepts
- Human-readable history
- Decentralized operation

The intention is not to duplicate Git but to extend Git-style workflows into project planning.

---

## Gradle Wrapper

The Gradle Wrapper heavily influenced OT installation and version selection.

Desirable properties include:

- Global launcher
- Project-specific version
- Reproducible execution
- Independent project upgrades

The OT launcher model was largely inspired by this workflow.

---

## Mercurial

Team experience with Mercurial influenced design goals.

Although Git receives higher implementation priority, OT attempts to avoid unnecessary Git-specific assumptions.

Examples:

- Repository root discovery
- Identity resolution
- Optional version control support

---

## Subversion

Experience with centralized version control systems influenced the requirement that OT must continue operating without distributed version control.

Subversion-style and patch-based workflows remain valid use cases.

---

## TFS

Experience with Team Foundation Server influenced the desire to avoid coupling work tracking to server-side infrastructure.

---

# Why OT Exists

A recurring problem with many planning systems is that planning information often becomes separated from development workflows.

Examples:

- Ticket systems
- Databases
- Wikis
- Spreadsheets

These systems frequently become disconnected from:

- Source code
- Pull requests
- Branches
- Releases

OT attempts to reduce this separation.

---

# Why Not A Database

The database option was discussed repeatedly.

Benefits considered:

- Centralized access
- Easy reporting
- Familiar architecture

Problems identified:

- Synchronization
- Availability
- Backups
- Migration
- Service ownership
- Authentication
- Multiple sources of truth

The repository already solves many of these problems.

For OT, a database feels like duplicated infrastructure.

---

# Why Not A Wiki

Wikis were considered valuable for presentation but less attractive as authoritative storage.

Concerns include:

- Data duplication
- Synchronization problems
- Review difficulty
- Branching limitations

Current preference:

```text
Repository → Wiki
```

rather than:

```text
Wiki → Repository
```

when synchronization is required.

---

# Why Push Is Less Attractive Than Pull

A recurring design theme is:

```text
Other systems pull from OT.
```

rather than:

```text
OT pushes into other systems.
```

Reasons include:

- Reduced maintenance burden
- Fewer integrations to support
- Smaller core system
- Clear ownership

The repository remains authoritative.

External systems may consume data independently.

---

# Import Philosophy

Importing is viewed differently than synchronization.

Current preference:

```text
Import
  ↓
Repository Changes
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

Repository review remains the authority.

Imported data should never bypass project review.

---

# Import Tooling

Importers are currently envisioned as separate tools.

Examples:

```text
jira-import
azure-devops-import
github-issues-import
```

These tools may eventually exist but are not considered part of the OT core.

---

# Why Human Readability Wins

Multiple discussions evaluated machine-efficient formats versus human-friendly formats.

Examples:

- JSON
- Databases
- Structured formats

The recurring conclusion was:

```text
Human readability is more important.
```

Reasons:

- Code reviews
- Direct editing
- Long-term durability
- Tool independence

Performance concerns can be addressed later if necessary.

---

# Work Item Evolution

## Original Model

Early versions used:

```text
Epic
Task
```

as separate concepts.

Bugs and enhancements were represented as task types.

---

## Current Direction

Current thinking treats everything as:

```text
WorkItem
```

with configurable types.

Reasons:

- Simpler hierarchy
- Less duplicated logic
- Easier nesting

---

# Relationship Evolution

Relationships started as:

```text
Epic
  Task
```

The model evolved toward:

```text
Parent
Child
Dependency
```

independent of item type.

This allows:

- Releases
- Epics
- Tasks
- Subtasks

to share the same structures.

---

# Identifier Evolution

## Original Direction

Earlier designs considered:

```text
Monotonic Numbers
```

Examples:

```text
OT-123
```

and:

```text
system.next_id_number
```

---

## Problems Identified

Issues:

- Merge conflicts
- Branch conflicts
- Distributed development
- Offline creation

---

## Current Direction

Current direction:

```text
UUID
```

plus:

```text
Git-style short identifiers
```

Questions remain regarding implementation details.

See:

- OQ-0008

---

# Filesystem Layout Evolution

Several layouts have been discussed.

Examples:

```text
Task.md
```

```text
Task/
  index.md
```

```text
Task.md
Task/
```

Current preference appears to be:

```text
Task/
  index.md
```

because it naturally supports:

- Attachments
- Child WorkItems
- Expansion over time

No final decision has been recorded yet.

---

# Why Validation Is So Important

A fundamental assumption in OT is:

```text
Users edit files directly.
```

This creates risks:

- Broken links
- Invalid metadata
- Invalid relationships

Instead of forbidding editing, OT emphasizes validation and repair.

This philosophy drives:

```text
ot check
ot check --fix
```

and much of the project's architecture.

---

# Why PRs Matter

A recurring theme throughout the design is:

```text
Review through Pull Requests.
```

This applies to:

- Code
- Work items
- Meetings
- Planning

PRs are viewed as the primary review and approval mechanism.

This allows planning to fit naturally into existing engineering workflows.

---

# Design Philosophy Summary

Several principles repeatedly appeared during discussions:

- Repository first
- Human readable first
- Git aware but not Git dependent
- Validation over restriction
- Pull rather than push
- Review through PRs
- Tool independence
- Distributed operation
- Minimal infrastructure
- Long-term durability

These principles should be used to evaluate future feature proposals.

When uncertain, prefer solutions that align with these principles.
