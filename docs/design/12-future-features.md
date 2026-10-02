# Future Features

## Purpose

This document captures potential future capabilities for Open Tasks (ot).

Items in this document are intentionally not commitments.

Inclusion in this document does not imply:

- Approval
- Prioritization
- Roadmap commitment
- Implementation intent

Many ideas recorded here may never be implemented.

The purpose is to preserve ideas without allowing them to distract from current development work.

---

# Feature Evaluation Criteria

Future features should be evaluated against OT's core principles:

- Repository native
- Human readable
- Tool independent
- Offline capable
- Minimal infrastructure
- Pull request friendly
- Source control friendly

Features that conflict with these principles require strong justification.

---

# Version Control Support

## Mercurial Support

Status:

Possible

Description:

Provide functionality similar to Git integration for Mercurial repositories.

Potential capabilities:

- Root discovery
- Identity discovery
- Editor discovery
- Safety-state detection

Related:

- ADR-0005 Git Preferred Integration

---

## Additional Version Control Systems

Status:

Possible

Examples:

- Subversion
- Perforce
- Fossil
- Future systems

Current expectation:

Unknown version control systems should behave similarly to "no version control".

---

# Attachments

## Rich Attachment Metadata

Status:

Possible

Description:

Allow metadata such as:

- Description
- Type
- Author
- Creation timestamp
- External vs local source

Related:

- OQ-0003 Attachment Metadata Model

---

## Attachment Preview Generation

Status:

Possible

Examples:

- Image previews
- Document thumbnails
- Diagram rendering

Goal:

Improve repository browsing and review experience.

---

## Attachment Deduplication

Status:

Possible

Description:

Identify duplicate attachments and suggest consolidation.

Requires future ownership and reference rules.

---

# Planning Features

## Sprint Management

Status:

Likely

Description:

Support sprint planning workflows.

Potential capabilities:

- Sprint definitions
- Sprint assignment
- Sprint reporting
- Sprint closure

Related:

- OQ-0004 Sprint Representation

---

## Burndown Reporting

Status:

Possible

Description:

Generate burndown charts from repository data.

Potential outputs:

- Markdown
- HTML
- Images

---

## Velocity Reporting

Status:

Possible

Description:

Generate historical metrics from completed work.

Possible metrics:

- Completed items
- Throughput
- Lead time
- Cycle time

---

## Capacity Planning

Status:

Possible

Description:

Assist teams in estimating future sprint capacity.

---

# Repository Analytics

## Project Health Reports

Status:

Possible

Description:

Generate project summaries from repository data.

Examples:

- Open work
- Blocked work
- Recently completed work
- Large unfinished items

---

## Dependency Analysis

Status:

Possible

Description:

Analyze dependency graphs and identify bottlenecks.

Examples:

- Circular dependencies
- Bottleneck work items
- High-risk work

---

## Work Item Visualization

Status:

Possible

Description:

Generate visual representations of:

- Hierarchies
- Dependencies
- Planning structures

Possible outputs:

- Mermaid diagrams
- Graphviz diagrams
- HTML visualizations

---

# Search and Discovery

## Full Repository Search

Status:

Likely

Description:

Search work items, meetings, comments, and attachments.

Potential examples:

```bash
ot search login

ot search --status blocked

ot search --type bug
```

---

## Relationship Exploration

Status:

Possible

Description:

Navigate dependency and hierarchy relationships interactively.

---

# Import Features

## Jira Import

Status:

Possible

Description:

Import Jira data into repository-native OT data.

Expected workflow:

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

---

## GitHub Issues Import

Status:

Possible

Description:

Convert GitHub Issues into OT WorkItems.

---

## Azure DevOps Import

Status:

Possible

Description:

Convert Azure DevOps work tracking data into OT WorkItems.

---

## Custom Import Framework

Status:

Possible

Description:

Allow external tools to generate OT-compatible repository content.

---

# Export Features

## Static Documentation Export

Status:

Possible

Description:

Generate static documentation from OT repositories.

Possible outputs:

- HTML
- PDF
- Markdown bundles

---

## Reporting Export

Status:

Possible

Description:

Generate structured exports.

Examples:

- CSV
- JSON
- XML

---

## Dashboard Integration

Status:

Possible

Description:

Allow external systems to consume OT repository data.

OT itself should not become a dashboard platform.

Related:

- ADR-0019 Export as a Separate Concern

---

# Artificial Intelligence Features

## Summary Generation

Status:

Possible

Description:

Generate summaries for:

- Work items
- Meetings
- Sprints

---

## Work Item Suggestions

Status:

Possible

Description:

Suggest:

- Missing subtasks
- Missing dependencies
- Related work

---

## Planning Assistance

Status:

Possible

Description:

Assist in grooming and planning activities.

Examples:

- Requirements analysis
- Dependency identification
- Risk discovery

---

# Plugin and Extension Support

## Plugin System

Status:

Uncertain

Description:

Allow extensions to add behavior without modifying OT.

Current concerns:

- Complexity
- Maintenance burden
- Security

Related:

- OQ-0018 Future Plugin and Extension Model

---

## Custom Commands

Status:

Possible

Description:

Allow projects to define additional commands.

---

# User Interfaces

## Terminal User Interface

Status:

Possible

Description:

Provide a terminal-based interface.

Examples:

- Task browsing
- Search
- Reporting

---

## Web Interface

Status:

Uncertain

Description:

Provide a browser-based view over repository data.

Current concern:

Avoid turning OT into a hosted service.

---

## Desktop Applications

Status:

Low Priority

Description:

Provide desktop tools for repository visualization.

---

# Explicit Non-Goals

The following remain out of scope unless future ADRs state otherwise:

- Database backends
- Hosted SaaS platforms
- Real-time collaborative editing
- Mandatory cloud services
- Bidirectional synchronization with external systems

See:

- ADR-0016 No Database Backend
- ADR-0019 Export as a Separate Concern

---

# Notes

Features should move from this document into:

- ADRs
- Design documents
- Roadmap phases

only after they become active design work.

Until then, this document serves as a holding area for future ideas.
