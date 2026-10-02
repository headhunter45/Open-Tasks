# Implementation Notes

## Purpose

This document is a temporary collection of implementation observations, ideas, assumptions, research topics, and reminders.

Unlike:

- ADRs
- Design documents
- Open Questions

the contents of this document are intentionally informal.

Items may:

- Become WorkItems
- Become ADRs
- Become Open Questions
- Be deleted

without further process.

This document should not be considered authoritative architecture.

---

# Current Status

The OT architecture has largely been defined.

The next phase is implementation.

The purpose of this document is to capture implementation concerns before they become formal tasks.

---

# Immediate Implementation Goal

Implement enough functionality that OT can begin tracking development of OT itself.

See:

- 13-proof-of-concept-scope.md

---

# Repository Setup

Potential repository structure:

```text
ot/
├─ src/
├─ tests/
├─ docs/
│  └─ design/
├─ scripts/
├─ examples/
└─ templates/
```

Needs review once implementation begins.

---

# Python Version

Open question:

What minimum Python version should OT require?

Initial expectation:

```text
Python 3.11+
```

Reasoning:

- Modern typing
- Dataclasses
- Good platform support
- Long support horizon

Need verification before final decision.

Possible future ADR.

---

# Packaging Investigation

Need to evaluate:

```text
Single Python Script
Zipapp
PEX
Self-contained archive
```

Goals:

- Avoid project-local virtual environments
- Minimize installation friction
- Support project-installed versions

Related:

- ADR-0009

---

# Markdown Libraries

Need to evaluate:

```text
markdown-it-py
mistune
python-markdown
```

Questions:

- Parsing capability
- Performance
- Round-trip support
- Extensibility

---

# Markdown Round Trip Preservation

Critical requirement:

Unknown content must survive editing.

Example:

```markdown
## User Notes

Anything written here.
```

OT should not destroy or reorder user content unnecessarily.

Need to investigate:

- AST approaches
- Parsing strategies
- Preservation techniques

---

# Frontmatter Format

Need to decide:

```text
YAML
JSON
Custom Format
```

Current assumption:

YAML is likely easiest for users.

Decision not finalized.

Potential future ADR.

---

# UUID Library

Need to evaluate:

```python
uuid.uuid4()
```

May be sufficient.

Need to determine whether additional hashing is desirable for short IDs.

See:

- OQ-0008

---

# Short Identifier Research

Need implementation spike.

Questions:

- Hash UUID?
- Truncate UUID?
- Minimum display length?
- Minimum accepted user prefix?

Need examples using realistic repository sizes.

---

# Work Item Recognition

Current assumption:

WorkItems are recognized by required metadata including UUID.

Need implementation prototype.

Questions:

- How expensive is repository scanning?
- How should invalid documents behave?

---

# Work Item Discovery

Need to evaluate:

```text
Filesystem Walking
Cached Index
Generated Manifest
```

Current preference:

Filesystem walking.

Avoid unnecessary indexes until performance requires them.

---

# Configuration System Implementation

Need implementation spike.

Requirements:

- Layer merging
- Override precedence
- Protected keys
- Validation

Investigate data structures.

---

# Protected Key Registry

Potential implementation:

```python
PROTECTED_KEYS = [...]
```

Need to evaluate:

- Hardcoded list
- Schema annotations
- Config metadata

---

# Validation Framework

Need architecture prototype.

Potential categories:

```text
Configuration
Filesystem
WorkItems
Meetings
Attachments
Templates
```

Need consistent reporting format.

---

# Validation Output Format

Potential structure:

```text
ERROR
WARNING
INFO
```

Need:

- Human-readable output
- Script-friendly output

Potential future:

```bash
--json
```

---

# Work Item Parser

Need proof of concept parser.

Responsibilities:

- Metadata extraction
- Comment handling
- Relationship handling
- Attachment handling

Unknown content preservation is critical.

---

# Templates

Need first template set.

Examples:

```text
WorkItem Template
Comment Template
Meeting Template
```

Keep initial templates intentionally simple.

---

# Meeting Implementation

Recommendation:

Do not implement first.

Complete WorkItem support before Meetings.

See:

- 13-proof-of-concept-scope.md

---

# Attachments

Recommendation:

Do not implement first.

Questions remain unresolved.

See:

- OQ-0002
- OQ-0003
- OQ-0017

---

# Upgrade System

Recommendation:

Do not implement first.

Get WorkItem persistence working before version-management complexity.

---

# Mercurial Support

Recommendation:

Design for it.

Do not implement it initially.

Git and no-VCS support is sufficient for validating architecture.

---

# Repository Scanning Performance

Do not optimize early.

Initial priorities:

- Correctness
- Simplicity
- Readability

Future optimization should be driven by real repository sizes.

---

# CLI Framework

Need evaluation.

Candidates:

```text
argparse
click
typer
```

Initial preference:

Unknown.

Requires investigation.

Recommendation:

Favor minimal dependencies.

---

# Logging

Need to determine:

```text
Python logging
Custom logging
Structured logging
```

Keep initial implementation simple.

---

# Testing Strategy

Need early decisions regarding:

```text
Unit Tests
Integration Tests
Filesystem Tests
Upgrade Tests
```

Repository behavior should be heavily tested.

---

# Cross Platform Testing

Target platforms:

```text
Linux
macOS
Windows
```

Need to ensure:

- Path handling
- Editor launching
- Wrapper behavior
- File locking

work consistently.

---

# File Locking

Need implementation research.

OT requires:

```text
Single OT process per project
```

Need cross-platform locking behavior.

See:

- ADR-0006
- 07-validation-and-repair.md

---

# Example Repository

Create a realistic test repository.

Examples:

- Multiple WorkItems
- Nested WorkItems
- Meetings
- Attachments

This repository should be used throughout development.

---

# Self Hosting Goal

Milestone:

OT should eventually manage OT development.

Success criteria:

New OT work should be tracked through OT rather than the current manual process.

This milestone marks successful validation of the core architecture.

See:

- 13-proof-of-concept-scope.md

---

# Notes For Future Me

Do not rush:

- Meetings
- Attachments
- Reporting
- Imports
- Exports
- Plugins

The project succeeds or fails based on:

- WorkItem persistence
- UUIDs
- Markdown editing
- Validation
- Repository workflows

Get those right first.
