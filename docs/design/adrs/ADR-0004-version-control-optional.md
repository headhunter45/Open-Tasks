# ADR-0004 - Version Control Optional

Status:
Accepted

Context:

Most intended users are expected to use Git.

However, OT should not require any specific version control system.

Some users may:

- Use Mercurial
- Use other version control systems
- Use no version control system
- Transfer repositories using archives or patches

Decision:

Version control support is optional.

OT must function without any version control system.

Reasoning:

Version control systems improve OT but should not be required for its operation.

The repository structure itself is sufficient for OT to function.

Alternatives Considered:

### Require Git

Pros:

- Simpler implementation
- Better integration

Cons:

- Excludes non-Git environments
- Creates unnecessary dependency

### Require Distributed Version Control

Pros:

- Simplifies some workflows

Cons:

- Still excludes valid users
- Provides little value over detecting available systems

Consequences:

Positive:

- Broader compatibility
- Simpler portability
- Archive-based workflows remain possible

Negative:

- Some features require fallback behavior
- Identity detection becomes more complex
