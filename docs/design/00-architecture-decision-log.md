# Architecture Decision Log

This document provides an index of Architecture Decision Records (ADRs) for Open Tasks (ot).

ADRs capture significant architectural decisions and the rationale behind them.

Design documents describe how the system works.

ADRs describe why the system works that way.

---

## Status Definitions

| Status | Description |
|----------|----------|
| Proposed | Decision is under consideration and not yet final. |
| Accepted | Decision has been agreed upon and should guide future design and implementation work. |
| Superseded | Decision has been replaced by a newer ADR. |
| Rejected | Decision was considered and intentionally not adopted. |

---

# ADR Index

| ADR | Title | Status |
|------|---------|---------|
| ADR-0001 | Repository Native Storage | Accepted |
| ADR-0002 | Markdown as Primary Storage Format | Accepted |
| ADR-0003 | Unified WorkItem Model | Accepted |
| ADR-0004 | Version Control Optional | Accepted |
| ADR-0005 | Git Preferred Integration | Accepted |
| ADR-0006 | DVCS Safety Model | Accepted |
| ADR-0007 | UUID Backed Identifiers | Accepted |
| ADR-0008 | Git Style Short Identifiers | Accepted |
| ADR-0009 | Project Installed Tool Versions | Accepted |
| ADR-0010 | Optional Wrapper Scripts | Accepted |
| ADR-0011 | Configuration Layering | Accepted |
| ADR-0012 | Configuration Precedence Order | Accepted |
| ADR-0013 | Project and User Configuration Separation | Accepted |
| ADR-0014 | Template Based Content Generation | Accepted |
| ADR-0015 | Transactional Upgrades | Accepted |
| ADR-0016 | Protected Configuration Keys | Accepted |
| ADR-0017 | Configuration Validation and Repair | Accepted |
| ADR-0018 | Import Through Repository Workflows | Accepted |
| ADR-0019 | Export as a Separate Concern | Accepted |
| ADR-0020 | Pull Requests as Review Authority | Accepted |
| ADR-0021 | Meeting Verification Through Repository Review | Accepted |
| ADR-0022 | Template Customization Over Code Customization | Accepted |
| ADR-0023 | First Class Validation and Repair | Accepted |
| ADR-0024 | Markdown First Editing Workflow | Accepted |
| ADR-0025 | Human Readable Over Machine Optimal | Accepted |
| ADR-0026 | Work Item Filesystem Ownership | Proposed |
| ADR-0027 | Direct File Editing Is Supported | Accepted |
| ADR-0028 | Project Root Discovery | Accepted |
| ADR-0029 | .ot Directory As Canonical Tool Root | Accepted |
| ADR-0030 | Identity and Editor Resolution | Accepted |

---

# Related Documents

The following design documents provide detailed implementation and behavioral guidance that expands on the decisions recorded in this ADR index.

Planned documents:

| Document | Purpose |
|------------|------------|
| 01-vision-and-philosophy.md | Project goals, principles, and non-goals |
| 02-filesystem-layout.md | Repository layout and storage structure |
| 03-configuration-system.md | Configuration hierarchy and behavior |
| 04-work-item-model.md | Work item structure and relationships |
| 05-meetings-and-planning.md | Meeting workflows and planning artifacts |
| 06-cli-reference.md | User-facing commands and workflows |
| 07-identity-resolution.md | User identity and editor discovery |
| 08-upgrade-and-versioning.md | Version management and migrations |
| 09-validation-and-repair.md | Integrity verification and repair behavior |
| 10-open-questions.md | Unresolved design questions |

---

# Modification Policy

When a significant architectural decision is made:

1. Create a new ADR.
2. Do not rewrite history in existing ADRs.
3. Mark superseded ADRs as Superseded rather than deleting them.
4. Update this index accordingly.

The purpose of the ADR system is to preserve the reasoning behind design decisions and provide historical context for future contributors.
`
