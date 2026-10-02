# ADR-0025 - Human Readable Over Machine Optimal

Status:
Accepted

Context:

Many implementation choices involve a tradeoff between:

- Human readability
- Machine efficiency

Examples include:

- Markdown storage
- Repository files
- Explicit relationships
- Template systems

Decision:

When practical, OT shall prefer human-readable solutions over machine-optimal solutions.

Reasoning:

OT is intended to be edited, reviewed, discussed, and maintained by humans.

Machine efficiency is important but secondary to accessibility.

Alternatives Considered:

### Machine Optimal Formats

Pros:

- Faster processing
- Reduced storage

Cons:

- Poor usability
- Reduced transparency

### Generated Internal Representations

Pros:

- Strong optimization

Cons:

- Additional complexity

Consequences:

Positive:

- Improved user experience
- Easier contribution
- Easier review

Negative:

- Some performance costs
- Additional validation logic
