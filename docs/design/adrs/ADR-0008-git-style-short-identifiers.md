# ADR-0008 - Git Style Short Identifiers

Status:
Accepted

Context:

UUIDs are not practical for daily use.

Users frequently need to:

- View work items
- Reference work items
- Create relationships
- Create dependencies

Typing full UUIDs is undesirable.

Decision:

OT shall expose short identifiers derived from canonical UUIDs.

Displayed identifiers shall be:

- Stable
- Unique within the current project
- Extended as necessary to avoid ambiguity

When users specify identifiers, OT shall accept the shortest unambiguous prefix.

Reasoning:

This mirrors the user experience provided by Git commit hashes.

Alternatives Considered:

### Monotonic Ticket Numbers

Pros:

- Familiar
- Human friendly

Cons:

- Coordination required
- Difficult merging

### User Chosen Identifiers

Pros:

- Flexible

Cons:

- Naming collisions
- Increased validation complexity

### Full UUID Usage

Pros:

- No ambiguity

Cons:

- Poor usability

Consequences:

Positive:

- Human friendly references
- Merge friendliness
- Distributed operation

Negative:

- Requires ambiguity detection
- Requires identifier resolution logic
