# ADR-0028 - Project Root Discovery

Status:
Accepted

Context:

OT commands may be executed from any directory inside a project.

The system requires a consistent method of locating the project root.

Decision:

OT shall discover project roots by traversing parent directories.

Recognition priority:

1. .ot
2. .git
3. .hg
4. Current working directory

Reasoning:

The project root should be discovered automatically whenever possible.

OT-specific data provides the strongest indication of an OT project.

Alternatives Considered:

### Explicit Project Root Only

Pros:

- Simple implementation

Cons:

- Poor user experience

### Git Root Only

Pros:

- Simple Git integration

Cons:

- Excludes non-Git projects

Consequences:

Positive:

- Consistent behavior
- Reduced configuration burden
- Supports DVCS and non-DVCS projects

Negative:

- Additional filesystem traversal
