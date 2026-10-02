# Validation and Repair

## Overview

This document describes validation and repair behavior within Open Tasks (ot).

Validation and repair are first-class features of OT.

Because OT explicitly supports:

- Direct editing
- Repository-native storage
- Manual modification of Markdown
- Manual modification of configuration files

the system must provide mechanisms to detect, report, and repair inconsistencies.

Related:

- ADR-0017 Configuration Validation and Repair
- ADR-0023 First Class Validation and Repair
- ADR-0027 Direct File Editing Is Supported

---

# Goals

The validation system should:

- Detect invalid project state
- Report actionable diagnostics
- Prevent silent corruption
- Support direct editing workflows
- Repair safe, deterministic problems
- Preserve user data whenever possible

The repair system should:

- Remain conservative
- Avoid destructive changes
- Explain all modifications
- Prefer warnings over automatic deletion

---

# Command Interface

## Validation

```bash
ot check
```

Checks project integrity without modifying files.

Expected output:

```text
Errors
Warnings
Recommendations
Summary
```

---

## Repair

```bash
ot check --fix
```

Performs validation and attempts to repair fixable issues.

Repair operations should be:

- Deterministic
- Safe
- Reversible through source control

Repairs should be reported to the user.

Example:

```text
Moved protected configuration key to project config.
Fixed broken work item reference.
Updated invalid attachment path.
```

---

# Validation Categories

Validation is divided into several categories.

---

# Configuration Validation

## Verify Configuration Files

Validate:

```text
.ot/config.json
.ot/config.local.json
~/.ot/config.json
```

Checks include:

- Valid JSON
- Schema version compatibility
- Required sections
- Unknown sections
- Duplicate values
- Invalid data types

---

## Configuration Layer Validation

Verify values exist in the correct configuration layer.

Examples:

Protected values found in:

```text
.ot/config.local.json
```

should generate warnings.

Examples:

```text
workItem.types
workItem.statuses
workItem.sizes
meeting.types
```

---

## Configuration Precedence Validation

Detect ineffective configuration values.

Example:

```text
A value overridden by a higher-precedence source.
```

These should typically be warnings rather than errors.

---

# Identity Validation

Validate identity information used by OT.

Examples:

```text
user.name
user.email
user.editor
```

Checks:

- Missing values
- Empty values
- Invalid formats where applicable

Missing identity information should generally produce warnings.

---

# Work Item Validation

## UUID Validation

All WorkItems must contain a valid UUID.

Checks:

- Missing UUID
- Invalid UUID
- Duplicate UUID

Duplicate UUIDs are errors.

Missing UUIDs cause content to be treated as ordinary Markdown rather than a WorkItem.

See:

- 04-work-item-model.md

---

## Type Validation

Verify:

```text
workItem.type
```

contains a valid configured type.

Unknown types are errors.

---

## Status Validation

Verify:

```text
workItem.status
```

contains a configured status.

Unknown statuses are errors.

---

## Size Validation

Verify:

```text
workItem.size
```

contains a configured size value.

Unknown sizes are errors.

---

## Relationship Validation

Validate:

- Parent references
- Child references
- Dependency references

Checks include:

```text
Missing WorkItems
Broken references
Circular references
Invalid relationships
```

Specific circular relationship rules remain under discussion.

---

# Dependency Validation

Validate dependency relationships.

Examples:

```text
Task A depends on Task B
```

Checks include:

- Missing targets
- Self-dependencies
- Duplicate relationships

Dependency cycles may be reported as warnings or errors depending on future policy.

---

# Filesystem Validation

## Project Structure

Validate required directories exist.

Examples:

```text
.ot/
.ot/tasks/
.ot/meetings/
.ot/templates/
```

Missing required directories are fixable.

---

## Work Item Structure

Validate:

- Work item locations
- Naming conventions
- Required files

Examples:

```text
Missing index.md
Invalid nesting
Unexpected structure
```

---

## File And Directory Name Conflicts

Detect cases such as:

```text
SomeTask.md
SomeTask/
```

within the same parent directory.

Behavior:

If:

```text
SomeTask/index.md
```

already exists:

```text
Non-fixable error
```

If:

```text
SomeTask/index.md
```

does not exist:

```text
Fixable warning
```

Potential repair:

```text
Move SomeTask.md → SomeTask/index.md
```

---

# Link Validation

Validate references contained in Markdown.

Examples:

```markdown
../SomeTask/index.md
```

Checks include:

- Missing files
- Missing targets
- Invalid relative paths

---

## Attachment Link Validation

Validate:

- Relative links
- Attachment references
- Expected attachment locations

Examples:

```text
Image referenced but file missing.
Attachment located outside expected ownership subtree.
```

---

# Attachment Validation

Validate attachment integrity.

Checks include:

- Missing files
- Invalid paths
- Invalid references
- Orphaned attachments

Examples:

```text
Attachment exists but is never referenced.
Attachment referenced but missing.
```

---

## Attachment Ownership Validation

Checks ownership expectations.

Examples:

```text
Attachment stored beneath one work item but referenced only by another.
```

Potential repair:

```text
Recommend relocation.
```

Automatic movement should be conservative.

See:

- OQ-0017 Attachment Ownership Rules

---

# Meeting Validation

Validate meeting records.

Checks include:

- Valid meeting type
- Valid timestamps
- Valid WorkItem references
- Valid attendees
- Valid attachments

Meeting validation should remain tolerant of manually written notes.

---

# Template Validation

Validate:

```text
.ot/templates/
```

Checks may include:

- Missing templates
- Invalid templates
- Missing required placeholders

Projects may intentionally customize templates.

Validation should focus on structural correctness rather than content.

---

# Version Validation

Validate project installation.

Checks include:

- Installed version matches configuration
- Required files exist
- Required runtime assets exist

Example:

```text
Configured version 1.3.0
Installed version 1.2.0
```

This is an error.

---

# Upgrade Validation

Validate upgrade state.

Checks include:

- Partially applied upgrades
- Schema mismatches
- Missing migration results

Detected inconsistencies should block normal operation.

---

# Merge Conflict Detection

Detect unresolved merge conflicts.

Examples:

```text
<<<<<<<
=======
>>>>>>>
```

Checks should include:

```text
.ot/config.json
.ot/config.local.json
WorkItem files
Meeting files
Templates
```

Unresolved conflicts are errors.

---

# DVCS Safety Validation

When operating within a recognized version control system:

- Git
- Mercurial

OT should detect unsafe states.

Examples:

```text
Merge
Rebase
Interactive Rebase
Cherry-Pick
Checkout
Repository Rewrite Operation
```

Unsafe states should block write operations.

Read-only commands may still be allowed.

Related:

- ADR-0006 DVCS Safety Model

---

# Repair Philosophy

Repairs should:

- Preserve user data
- Avoid removing content unnecessarily
- Be deterministic
- Be explainable

Source control should remain the primary recovery mechanism.

---

# Fixable Issues

Examples:

```text
Missing directory
Incorrect configuration placement
Broken relative link
Missing generated file
Recoverable attachment location
```

These may be repaired automatically.

---

# Non-Fixable Issues

Examples:

```text
Conflicting identifiers
Duplicate UUIDs
Ambiguous ownership
Corrupted metadata
Incompatible schemas
```

These require user intervention.

---

# Reporting

Validation results should be categorized:

```text
Error
Warning
Information
```

Errors prevent correct operation.

Warnings indicate potentially undesirable states.

Information messages provide recommendations.

---

# Future Validation Areas

Potential future validation may include:

- Sprint validation
- Reporting validation
- Plugin validation
- Import validation
- Export validation

---

# Open Questions

Related open questions:

- OQ-0003 Attachment Metadata Model
- OQ-0004 Sprint Representation
