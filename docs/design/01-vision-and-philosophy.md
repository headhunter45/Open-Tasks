# Vision and Philosophy

## What Is Open Tasks?

Open Tasks (ot) is a repository-native planning, task tracking, and meeting management system.

OT stores project planning information as files that live alongside source code and participate in existing development workflows.

The repository itself is the source of truth.

Examples of information managed by OT include:

- Work items
- Tasks
- Bugs
- Enhancements
- Epics
- Planning notes
- Meeting records
- Sprint data
- Templates
- Attachments

OT treats planning artifacts as project assets rather than application data.

---

## Vision

Enable development teams to manage planning and project coordination using the same workflows they already use for source code.

A work item should be reviewable, branchable, mergeable, searchable, and auditable in the same manner as source code.

Planning should not require a separate hosted service, proprietary backend, or continuously available network connection.

---

## Goals

### Repository-Native Planning

Store planning information in the repository.

Project history should be captured by the version control system rather than a separate database.

---

### Human Readable Data

Project data should remain understandable without OT.

Users should be able to:

- Read work items directly
- Read meeting notes directly
- Review planning changes directly
- Search project history directly

---

### Tool Independence

The repository should remain useful even when OT is unavailable.

Users should be able to:

- Use standard text editors
- Use GitHub rendering
- Use GitLab rendering
- Use Obsidian
- Use repository viewers

without requiring OT.

---

### Offline First Operation

OT should support workflows that do not require network connectivity.

Work items should be creatable, editable, and reviewable without access to external services.

---

### Distributed Workflows

OT should work naturally with:

- Feature branches
- Pull requests
- Forks
- Patch-based workflows
- Archive-based workflows

No central coordinator should be required for normal operation.

---

### Long-Term Durability

Project planning information should remain useful decades later.

Users should not require:

- A specific service
- A specific vendor
- A specific website
- A specific database

to access historical project information.

---

## Design Principles

### Tasks as Source Code

Tasks should behave like source code.

Users should be able to:

- Branch tasks
- Review tasks
- Merge tasks
- Audit task history

using workflows already familiar to development teams.

See:

- ADR-0001
- ADR-0016
- ADR-0020

---

### Meetings as Source Code

Meeting outcomes are project decisions.

Meeting records should be stored, reviewed, and audited in the same way as code changes.

See:

- ADR-0021

---

### Human Readable Before Machine Optimal

When practical, OT favors solutions that improve human understanding over solutions that primarily optimize machine efficiency.

Examples include:

- Markdown files
- Explicit relationships
- Repository-native storage
- Template systems

See:

- ADR-0025

---

### Direct Editing Is A Feature

Manual modification of project files is a supported workflow.

OT should validate and repair project state rather than prevent users from editing their own data.

See:

- ADR-0027
- ADR-0023

---

### Use Existing Workflows

OT should integrate with workflows teams already understand.

Examples:

- Pull requests
- Code review
- Branching
- Merge workflows

Users should not be forced to learn a completely separate planning ecosystem.

---

### Favor Convention Over Complexity

OT should prefer simple, understandable conventions over highly configurable systems whenever practical.

Configuration should exist where it provides meaningful value.

Complexity requires strong justification.

---

### Minimize Required Infrastructure

OT should not require:

- Databases
- Application servers
- Hosted services
- Dedicated storage systems

for normal operation.

See:

- ADR-0016

---

## Non-Goals

### OT Is Not Jira

OT may solve some of the same problems as Jira, but it is not intended to reproduce every Jira feature.

OT prioritizes repository-native workflows instead of centralized issue tracking.

---

### OT Is Not A Database

Repository files are the system of record.

Database-backed storage is intentionally out of scope.

See:

- ADR-0016

---

### OT Is Not A Hosted Service

OT should function without requiring a SaaS platform.

Hosted services may interact with OT repositories, but OT itself is repository-centric.

---

### OT Is Not A Real-Time Collaboration Platform

OT does not attempt to provide:

- Real-time editing
- Presence awareness
- Multi-user document sessions

Teams should use existing collaboration tools when those capabilities are required.

---

### OT Is Not A Project Management Replacement For Every Team

OT is designed primarily for software development teams that already use source control and pull-request workflows.

Teams with fundamentally different workflows may be better served by other tools.

---

## Import Philosophy

Users should be able to migrate into OT.

Imported data should ultimately become repository content.

Repository review remains the authoritative validation mechanism.

See:

- ADR-0018

---

## Export Philosophy

OT data should be easy for external systems to consume.

Exporters may publish OT data into:

- Wikis
- Dashboards
- Reporting systems
- Issue trackers

These integrations are separate concerns from OT itself.

See:

- ADR-0019

---

## Version Control Philosophy

OT is version-control aware but not version-control dependent.

Current priority:

1. Git
2. No version control
3. Mercurial
4. Other supported systems

Projects without version control remain first-class citizens.

See:

- ADR-0004
- ADR-0005

---

## Success Criteria

OT will be considered successful if a team can:

1. Clone a repository.
2. Read project planning information with standard tools.
3. Create and modify work items.
4. Conduct planning meetings.
5. Review changes through pull requests.
6. Understand project history through repository history.
7. Continue working if OT itself becomes temporarily unavailable.

The repository should remain the authoritative source of project knowledge.
