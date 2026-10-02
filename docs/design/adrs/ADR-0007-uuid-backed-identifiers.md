# ADR-0007 - UUID Backed Identifiers

Status:
Accepted

Context:

Work items require stable identifiers.

The identifier system must support:

- Offline creation
- Merging
- Branching
- Distributed development

without requiring centralized coordination.

Decision:

Every work item shall contain a UUID.

The UUID is the canonical identifier used internally by OT.

Reasoning:

UUIDs provide globally unique identifiers without requiring a shared service, central database, or allocation server.

Alternatives Considered:

### Monotonic Numeric IDs

Pros:

- Human friendly
- Familiar to many users

Cons:

- Merge conflicts
- Coordination required
- Difficult offline operation

### Repository-Wide Counters

Pros:

- Simple implementation

Cons:

- Merge conflicts
- Concurrency challenges

### Hierarchical IDs

Pros:

- Human readable

Cons:

- Difficult to maintain
- Renaming issues
- Parent movement affects identifiers

Consequences:

Positive:

- Globally unique identifiers
- No central coordination
- Branch-friendly

Negative:

- Less human friendly
- Requires secondary display identifiers
