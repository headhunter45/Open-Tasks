# ADR-0026 - Work Item Filesystem Ownership

Status:
Proposed

Context:

Work items may contain:

- Child work items
- Attachments
- Additional generated content
- Future metadata

The filesystem layout must support hierarchical organization while remaining understandable to users.

Decision:

Each work item owns a subtree of the filesystem.

Files and folders associated with a work item should be stored within that work item's subtree.

Reasoning:

A work item represents a logical unit of work.

Keeping related content together improves:

- Discoverability
- Validation
- Refactoring
- Portability

Alternatives Considered:

### Flat Filesystem

Pros:

- Simple layout

Cons:

- Difficult attachment organization
- Difficult nesting

### Central Attachment Storage

Pros:

- Easier deduplication

Cons:

- Weaker ownership model
- Harder navigation

Consequences:

Positive:

- Clear ownership boundaries
- Natural hierarchy
- Easier validation

Negative:

- Filesystem layout rules become more important

Open Questions:

- Final directory structure
- Attachment placement rules
- Child work item representation
