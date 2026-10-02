# ADR-0029 - .ot Directory As Canonical Tool Root

Status:
Accepted

Context:

OT requires a predictable location for:

- Configuration
- Work items
- Templates
- Meetings
- Installed tool versions

Decision:

The .ot directory shall be the canonical OT project root.

All OT-owned project data shall exist within or beneath .ot unless explicitly relocated through configuration.

Reasoning:

A single root directory simplifies:

- Discovery
- Validation
- Upgrades
- Migration
- Backup

Alternatives Considered:

### Multiple Special Directories

Pros:

- Flexible layout

Cons:

- Harder discovery
- Harder upgrades

### Hidden Files Throughout Repository

Pros:

- Minimal central structure

Cons:

- Difficult maintenance

Consequences:

Positive:

- Easier tooling
- Consistent structure
- Easier onboarding

Negative:

- Large projects may accumulate many files beneath .ot
