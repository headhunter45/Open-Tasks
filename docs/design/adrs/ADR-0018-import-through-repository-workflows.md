# ADR-0018 - Import Through Repository Workflows

Status:
Accepted

Context:

Organizations adopting OT may already have planning data stored in:

- Jira
- Azure DevOps
- GitHub Issues
- Trello
- Wikis
- Custom tracking systems

Migration support may be desirable.

The system of record for OT remains the repository.

Decision:

Imports shall ultimately produce repository file changes.

Imported content shall be reviewed through normal repository workflows before becoming authoritative.

OT itself is not responsible for maintaining synchronization with external systems.

Reasoning:

Repository review remains the primary quality control mechanism for project data.

Imports should not bypass normal review processes.

Alternatives Considered:

### Direct Database Synchronization

Pros:

- Continuous updates

Cons:

- Additional complexity
- Multiple sources of truth

### Direct External System Integration

Pros:

- Improved interoperability

Cons:

- Long-term maintenance burden
- Increased scope

Consequences:

Positive:

- Consistent review process
- Single source of truth
- Simpler architecture

Negative:

- Migration tooling may require additional work
- Imports remain a user-driven process
