# ADR-0027 - Direct File Editing Is Supported

Status:
Accepted

Context:

OT stores project information in repository files.

Users may wish to:

- Edit work items manually
- Modify meeting notes directly
- Change templates without OT commands

Decision:

Direct file editing is a supported workflow.

OT validates and repairs project state rather than preventing manual modification.

Reasoning:

Users should retain ownership of their data.

Project data should remain useful even when OT is unavailable.

Alternatives Considered:

### OT Only Editing

Pros:

- Easier validation

Cons:

- Reduced transparency
- Tool dependence

### Read-Only Files

Pros:

- Strong consistency

Cons:

- Contradicts repository-native philosophy

Consequences:

Positive:

- Tool independence
- Easier collaboration
- Better interoperability

Negative:

- Increased validation requirements
- Additional repair logic required
