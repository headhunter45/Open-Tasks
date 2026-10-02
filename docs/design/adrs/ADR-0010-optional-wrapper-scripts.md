# ADR-0010 - Optional Wrapper Scripts

Status:
Accepted

Context:

Many development environments support globally installed tools.

Some environments do not:

- Shared CI systems
- Hosted CI systems
- Managed corporate machines
- Locked-down developer environments

Decision:

Project-local wrapper scripts are optional.

Recommended names:

- otw
- otw.bat

The primary interface remains the globally installed `ot` command.

Reasoning:

Most users should not need wrapper scripts.

Projects may choose to include wrappers where deployment constraints require them.

Alternatives Considered:

### Project Wrapper Required

Pros:

- Consistent execution

Cons:

- Additional repository clutter
- Additional maintenance

### Global Installation Required

Pros:

- Minimal project files

Cons:

- Poor CI support
- Additional setup requirements

Consequences:

Positive:

- Flexible deployment
- Improved CI compatibility
- Reduced repository requirements

Negative:

- Multiple execution patterns
- Additional wrapper maintenance when used
