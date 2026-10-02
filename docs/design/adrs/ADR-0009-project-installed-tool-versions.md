# ADR-0009 - Project Installed Tool Versions

Status:
Accepted

Context:

Projects may require different OT versions.

A user's globally installed OT version may not match the version expected by all projects.

Decision:

Projects shall install their configured OT implementation under:

.ot/bin

The globally installed OT executable is a wrapper responsible for locating and invoking the expected project version.

Reasoning:

Projects should remain independent of user workstation upgrades.

Alternatives Considered:

### Single Global Installation

Pros:

- Simple deployment

Cons:

- Difficult upgrades
- Project incompatibility

### Python Package Per Project

Pros:

- Strong isolation

Cons:

- High storage overhead
- Additional virtual environments

### Bundled Runtime Per Project

Pros:

- Full isolation

Cons:

- Significant duplication
- Large project footprint

Consequences:

Positive:

- Version consistency
- Repeatable project behavior
- Reduced upgrade risk

Negative:

- Multiple copies of OT may exist
- Upgrade logic required
