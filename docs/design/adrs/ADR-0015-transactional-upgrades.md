# ADR-0015 - Transactional Upgrades

Status:
Accepted

Context:

OT upgrades may involve:

- Tool version changes
- Configuration migrations
- Template updates
- Filesystem layout changes

Failed upgrades must not leave projects in an inconsistent state.

Decision:

OT upgrades shall be transactional.

Upgrade activities shall occur in a temporary location until validation succeeds.

The existing installation remains unchanged until completion of the upgrade.

Reasoning:

Partially applied upgrades create difficult recovery scenarios and can corrupt project state.

Alternatives Considered:

### In-Place Upgrades

Pros:

- Simpler implementation

Cons:

- Risk of partial upgrades
- Difficult rollback

### Automatic Rollback

Pros:

- Better recovery

Cons:

- Additional complexity
- More failure modes

Consequences:

Positive:

- Safe upgrades
- Deterministic behavior
- Easier recovery

Negative:

- Increased implementation complexity
- Additional temporary storage requirements
