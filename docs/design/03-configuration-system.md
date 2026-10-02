# Configuration System

## Overview

This document describes the Open Tasks (ot) configuration system.

The configuration system is responsible for:

- Project configuration
- User preferences
- Identity information
- Editor configuration
- Work item definitions
- Meeting definitions
- Future system customization

Configuration is designed to support:

- Repository-native workflows
- Team-specific customization
- User-specific overrides
- Direct file editing
- Validation and repair

Related:

- ADR-0011 Configuration Layering
- ADR-0012 Configuration Precedence Order
- ADR-0013 Project and User Configuration Separation
- ADR-0016 Protected Configuration Keys
- ADR-0017 Configuration Validation and Repair
- ADR-0030 Identity and Editor Resolution

---

# Design Goals

The configuration system should:

- Support repository-wide defaults
- Support user-specific preferences
- Avoid repository noise
- Remain human readable
- Be editable without OT
- Be easy to validate
- Evolve over time through schema migration

Configuration files should remain understandable in a text editor.

---

# Configuration Files

## Repository Configuration

Location:

```text
.ot/config.json
```

Source Control:

```text
Committed
```

Purpose:

Project-wide configuration.

Examples:

- Work item types
- Work item statuses
- Work item sizes
- Meeting types
- Template configuration
- Repository layout configuration
- System metadata

---

## Repository Local Overrides

Location:

```text
.ot/config.local.json
```

Source Control:

```text
Ignored
```

Purpose:

Per-user configuration for the current checkout.

Examples:

- User name
- User email
- Preferred editor
- Local workflow preferences

---

## Global User Configuration

Location:

```text
~/.ot/config.json
```

Source Control:

```text
Not applicable
```

Purpose:

Reusable defaults for all OT projects used by a user.

Examples:

- User identity
- Editor preferences
- Personal defaults

---

# Configuration Resolution

Configuration values are resolved using the following precedence order:

```text
1. .ot/config.local.json
2. .ot/config.json
3. ~/.ot/config.json
4. VCS Commands
5. Environment Variables
6. System Defaults
```

The first value found wins.

This resolution process applies individually for each configuration field.

---

# Example Resolution

Example:

```text
user.editor
```

Resolution proceeds:

```text
.ot/config.local.json
    ↓
.ot/config.json
    ↓
~/.ot/config.json
    ↓
git config core.editor
    ↓
hg config ui.editor
    ↓
EDITOR
    ↓
VISUAL
    ↓
Platform Default
```

The first valid value is used.

---

# Configuration Sections

## user

The `user` section contains identity and preference information.

Example:

```json
{
  "user": {
    "name": "Tom",
    "email": "tom@example.com",
    "editor": "code"
  }
}
```

Typical fields:

```text
user.name
user.email
user.editor
```

These values are generally expected to be overridden locally.

---

## system

The `system` section contains OT system information.

Examples:

```text
Schema Versions
Migration Information
Internal Metadata
Future Runtime Configuration
```

Example:

```json
{
  "system": {
    "configSchemaVersion": 1
  }
}
```

Current contents remain subject to change.

See:

- OQ-0007 Configuration Schema Evolution

---

## workItem

The `workItem` section contains work item definitions.

Examples:

```json
{
  "workItem": {
    "types": {},
    "statuses": {},
    "sizes": {}
  }
}
```

---

### workItem.types

Defines valid work item types.

Example:

```json
{
  "bug": {
    "label": "Bug",
    "description": "A defect requiring correction."
  }
}
```

Examples:

```text
bug
enhancement
epic
task
spike
chore
```

Projects may define custom types.

---

### workItem.statuses

Defines valid status values.

Example:

```json
{
  "triage": {
    "label": "Triage",
    "description": "Waiting for review."
  }
}
```

Projects may customize statuses.

---

### workItem.sizes

Defines valid sizing values.

Example:

```json
{
  "small": {
    "label": "Small",
    "description": "A small amount of effort."
  }
}
```

Projects may define sizing systems appropriate to their workflow.

---

## meeting

The `meeting` section contains meeting definitions.

Example:

```json
{
  "meeting": {
    "types": {}
  }
}
```

---

### meeting.types

Defines meeting types.

Examples:

```text
grooming
planning
retrospective
ideation
```

Projects may introduce additional meeting types.

---

# Protected Configuration Keys

Some configuration values represent shared project behavior.

Examples:

```text
workItem.types
workItem.statuses
workItem.sizes
meeting.types
```

These values are considered protected.

Protected values should normally be defined in:

```text
.ot/config.json
```

rather than local override files.

See:

- ADR-0016 Protected Configuration Keys

---

# Improper Override Detection

OT validation should detect protected values defined in locations intended for local overrides.

Example:

```text
.ot/config.local.json
```

contains:

```text
workItem.statuses
```

This is considered an improper override.

OT should report this condition.

Example:

```text
Warning:
Protected configuration key overridden locally.
```

---

# Automatic Repair

The following command is expected to validate and correct configuration placement:

```text
ot check --fix
```

Potential repairs include:

- Moving protected values
- Removing duplicate values
- Removing obsolete values

Repair behavior should remain conservative.

See:

- ADR-0017 Configuration Validation and Repair

---

# Identity Resolution

OT requires identity information for:

- Comments
- Meeting attendance
- Audit records

Resolution uses:

```text
Project Local Config
    ↓
Project Config
    ↓
Global Config
    ↓
Git Configuration
    ↓
Mercurial Configuration
    ↓
Environment
    ↓
System Defaults
```

When available, Git and Mercurial should be queried using their command-line interfaces rather than direct configuration parsing.

Examples:

```text
git config user.name
git config user.email
git config core.editor

hg config ui.username
hg config ui.editor
```

See:

- ADR-0030 Identity and Editor Resolution

---

# Environment Variable Fallbacks

Potential environment variables include:

```text
EDITOR
VISUAL
EMAIL
```

Environment variables are only used if higher-priority sources do not provide values.

---

# System Defaults

If a value cannot be resolved elsewhere, system defaults may be used.

Examples:

Linux/macOS/BSD:

```text
nano
vi
```

Windows:

```text
notepad.exe
```

User names may be obtained through operating system APIs.

---

# Schema Versioning

Configuration files include schema information.

Schema versions are used to:

- Detect incompatible configurations
- Perform migrations
- Validate upgrades

Exact schema version structure remains under discussion.

See:

- OQ-0007 Configuration Schema Evolution

---

# Upgrade Behavior

Upgrades may perform:

- Configuration migration
- Default value updates
- Schema changes

Upgrades must be transactional.

A failed migration must leave the existing configuration unchanged.

See:

- ADR-0015 Transactional Upgrades

---

# Validation Requirements

The following are expected to be validated:

- Valid JSON
- Required sections
- Supported schema version
- Valid enum definitions
- Valid references
- Protected key placement
- Duplicate definitions
- Invalid overrides

Validation is provided through:

```text
ot check
ot check --fix
```

See:

- ADR-0023 First Class Validation and Repair

---

# Open Questions

The following configuration topics remain unresolved:

- OQ-0007 Configuration Schema Evolution
- OQ-0016 Repository Layout Overrides

Additional configuration sections may be introduced as OT evolves.
