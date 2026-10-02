# ADR-0020 - Pull Requests as Review Authority

Status:
Accepted

Context:

OT stores planning data as repository content.

Changes to planning information should be reviewed similarly to source code changes.

Decision:

Pull requests shall be treated as the preferred review mechanism for OT data.

Changes to:

- Work items
- Meeting records
- Planning documents
- Templates
- Configuration

should be reviewed through pull requests whenever practical.

Reasoning:

Development teams already understand pull request workflows.

Using existing review processes reduces cognitive overhead.

Alternatives Considered:

### Separate Approval Systems

Pros:

- Specialized workflows

Cons:

- Additional systems
- Duplicate review processes

### No Review Requirement

Pros:

- Faster changes

Cons:

- Reduced accountability
- Reduced auditability

Consequences:

Positive:

- Review history
- Discussion history
- Consistent approval process

Negative:

- Additional process overhead for small teams
