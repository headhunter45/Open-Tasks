# ADR-0012 - Configuration Precedence Order

Status:
Accepted

Context:

Multiple configuration layers require predictable resolution rules.

Users must be able to determine where a value originates and how to override it.

Decision:

Configuration values shall be resolved in the following order:

1. .ot/config.local.json
2. .ot/config.json
3. ~/.ot/config.json
4. Supported version control commands
5. Environment variables
6. System defaults

Reasoning:

Project-local overrides should take highest priority.

Repository configuration should provide shared project defaults.

User configuration should provide personal defaults.

Automatically discovered values should only be used when explicit configuration is unavailable.

Alternatives Considered:

### User Configuration Before Repository Configuration

Pros:

- Strong user customization

Cons:

- Reduced project consistency

### Environment Variables Before Configuration Files

Pros:

- Familiar to some tools

Cons:

- Difficult to reason about
- Hidden configuration

Consequences:

Positive:

- Deterministic configuration resolution
- Predictable customization
- Easier debugging

Negative:

- Requires documentation
- Requires configuration inspection tooling
