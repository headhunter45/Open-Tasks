# Proof of Concept Scope

## Purpose

This document defines the minimum functionality required for the first usable version of Open Tasks (ot).

The purpose of the Proof of Concept (PoC) is to validate the core architecture and workflows of OT.

The PoC is not intended to be feature complete.

Features outside this scope should generally be deferred until the core system is functional and validated.

---

# Goals

The Proof of Concept should answer the following questions:

1. Can OT persist WorkItems in a repository?
2. Can WorkItems be loaded and discovered reliably?
3. Can users interact with WorkItems using short identifiers?
4. Can users edit WorkItems directly and still maintain consistency?
5. Can OT support repository-native workflows without a database?
6. Does the WorkItem model support real-world planning needs?

If these questions are answered successfully, the core architecture can be considered validated.

---

# Success Criteria

The PoC is considered successful when a user can:

1. Initialize a project.
2. Create WorkItems.
3. List WorkItems.
4. View WorkItems.
5. Edit WorkItems.
6. Validate repository state.
7. Store all project data in the repository.
8. Use OT without a database.
9. Use OT without a web service.

---

# Included Features

## Project Initialization

Commands:

```bash
ot init
```

Capabilities:

- Create .ot directory
- Create configuration files
- Install templates
- Create required folders

---

## WorkItem Creation

Commands:

```bash
ot task create
```

Capabilities:

- Create WorkItems
- Generate UUIDs
- Generate short identifiers
- Apply templates

---

## WorkItem Discovery

Commands:

```bash
ot task list
```

Capabilities:

- Discover WorkItems
- Load WorkItems
- Display summaries

---

## WorkItem Viewing

Commands:

```bash
ot task show
```

Capabilities:

- Render WorkItem details
- Resolve short identifiers
- Display metadata

---

## WorkItem Editing

Commands:

```bash
ot task edit
```

Capabilities:

- Edit WorkItems
- Validate changes
- Save changes

---

## Status Updates

Commands:

```bash
ot task status
```

Capabilities:

- Modify status values
- Validate status definitions

---

## Comments

Commands:

```bash
ot task comment
```

Capabilities:

- Create comments
- Timestamp comments
- Record author information

---

## Relationship Management

Commands:

```bash
ot task add-dependency
ot task remove-dependency
ot task get-dependencies
```

Capabilities:

- Create relationships
- Remove relationships
- Query relationships

---

## Validation

Commands:

```bash
ot check
ot check --fix
```

Capabilities:

- Validate WorkItems
- Validate relationships
- Validate configuration
- Repair simple issues

---

# Included Data Model

The PoC includes:

```text
WorkItem
```

Types:

```text
task
bug
enhancement
epic
spike
chore
```

Additional types may be configured.

---

# Included Storage

Repository storage:

```text
.ot/
```

including:

```text
config.json
config.local.json
tasks/
templates/
```

The exact WorkItem layout may evolve during the PoC.

---

# Included Identifier System

WorkItems shall have:

```text
UUID
```

and:

```text
Short Identifier
```

Short identifiers may change implementation during the PoC.

The architecture decision to use UUIDs is considered settled.

See:

- ADR-0007
- ADR-0008

---

# Included Configuration

The PoC includes:

```text
Project Configuration
Project Local Overrides
Global User Configuration
```

Core configuration behavior should be validated.

---

# Deferred Features

The following features are intentionally deferred.

Deferred does not mean rejected.

---

## Meeting Management

Commands:

```text
ot meeting start
ot meeting end
ot meeting list
```

Status:

Deferred

Reason:

WorkItem persistence must be proven first.

---

## Sprint Management

Status:

Deferred

Reason:

Sprint model is unresolved.

See:

- OQ-0004

---

## Attachment Management

Commands:

```text
ot attachment *
```

Status:

Deferred

Reason:

Attachment ownership and metadata models remain unresolved.

See:

- OQ-0002
- OQ-0003
- OQ-0017

---

## Version Upgrades

Commands:

```text
ot upgrade
```

Status:

Deferred

Reason:

Version management can be implemented after WorkItem persistence is proven.

---

## Template Migration

Status:

Deferred

Reason:

Migration strategy is unresolved.

---

## Import Tooling

Status:

Deferred

Examples:

```text
Jira
Azure DevOps
GitHub Issues
```

Reason:

Core storage model must stabilize first.

---

## Export Tooling

Status:

Deferred

Reason:

Core repository format must stabilize first.

---

## Mercurial Support

Status:

Deferred

Reason:

Git and no-VCS workflows are sufficient for validating architecture.

---

## Additional VCS Support

Status:

Deferred

Reason:

Core repository model should be proven first.

---

## Plugin System

Status:

Deferred

Reason:

Premature abstraction.

---

## Reporting

Status:

Deferred

Examples:

```text
Burndown
Velocity
Analytics
Dashboards
```

Reason:

Requires stable data model first.

---

## Web Interface

Status:

Deferred

Reason:

Repository-native workflow takes priority.

---

## Desktop Applications

Status:

Deferred

Reason:

CLI-first implementation is preferred.

---

# Explicit Non-Goals For The PoC

The PoC does not attempt to prove:

- Team scaling
- Performance at large repository sizes
- Real-time collaboration
- Hosted service operation
- Enterprise integrations
- Database backends

These concerns are intentionally outside the first implementation phase.

---

# Exit Criteria

The PoC phase is complete when:

- Core WorkItem workflows are functioning.
- Repository persistence is stable.
- Validation is functional.
- Direct editing is validated.
- The architecture can be used to track OT development itself.

At that point OT should begin managing its own development tasks and future work through OT-managed WorkItems.

This milestone represents the transition from architectural validation to product development.
