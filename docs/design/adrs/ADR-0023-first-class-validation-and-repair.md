# ADR-0023 - First Class Validation And Repair

Status:
Accepted

Context:

OT encourages users to edit files directly.

Direct edits may create:

- Broken references
- Invalid statuses
- Invalid identifiers
- Invalid relationships

Decision:

Validation and repair are first-class responsibilities of the OT toolset.

Commands such as:

- ot check
- ot check --fix

are core functionality rather than optional utilities.

Reasoning:

Manual editing is a design goal.

Validation is required to support that goal safely.

Alternatives Considered:

### Restrict Direct Editing

Pros:

- Fewer errors

Cons:

- Conflicts with repository-native philosophy

### Detection Only

Pros:

- Simpler implementation

Cons:

- More user effort

Consequences:

Positive:

- Safe manual editing
- Consistent project state
- Better user experience

Negative:

- Additional implementation effort
- Requires careful repair logic
