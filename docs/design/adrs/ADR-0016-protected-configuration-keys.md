# ADR-0016 - Protected Configuration Keys

Status:
Accepted

Context:

Certain configuration values define shared project behavior.

Examples include:

- Work item types
- Work item statuses
- Work item sizes
- Meeting types
- Identifier formats

Allowing users to override these values locally can create confusion and inconsistent behavior.

Decision:

OT shall classify certain configuration values as protected.

Protected values may still be overridden, but:

- Warnings shall be emitted
- Validation shall report improper placement
- Automatic repair may move values to the correct configuration file

Reasoning:

OT should encourage project-level consistency without preventing local customization.

Alternatives Considered:

### Completely Forbid Overrides

Pros:

- Maximum consistency

Cons:

- Difficult to enforce
- Conflicts with OT's override philosophy

### Allow All Overrides Silently

Pros:

- Simple implementation

Cons:

- Increased user confusion
- Harder debugging

Consequences:

Positive:

- Consistent project behavior
- Actionable warnings
- Better validation

Negative:

- More complex validation logic
