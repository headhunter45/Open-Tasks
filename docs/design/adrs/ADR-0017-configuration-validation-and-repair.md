# ADR-0017 - Configuration Validation and Repair

Status:
Accepted

Context:

Users may edit configuration files manually.

Configuration drift can occur through:

- Merge conflicts
- Manual edits
- Incorrect overrides
- Upgrades

Decision:

OT shall provide validation and repair capabilities.

Primary commands include:

- ot check
- ot check --fix

Reasoning:

Manual editing is an intentional design goal.

Validation tooling is required to maintain consistency.

Alternatives Considered:

### Disallow Manual Editing

Pros:

- Reduced corruption risk

Cons:

- Contradicts OT philosophy

### Validation Without Repair

Pros:

- Simpler implementation

Cons:

- Increased user work

Consequences:

Positive:

- Better user experience
- Faster recovery
- Improved consistency

Negative:

- More implementation effort
- Repair rules must remain conservative
