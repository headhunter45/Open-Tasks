# ADR-0013 - Project and User Configuration Separation

Status:
Accepted

Context:

Some configuration is intended to be shared by all contributors.

Other configuration only applies to a specific user or checkout.

Examples:

Project Configuration:

- Work item types
- Status values
- Size values
- Templates
- System metadata

User Configuration:

- User name
- User email
- Preferred editor

Decision:

Store project and user configuration separately.

Project configuration:

- .ot/config.json

Project-local user overrides:

- .ot/config.local.json

Global user configuration:

- ~/.ot/config.json

Reasoning:

Project data should be reviewable and versioned.

User preferences should remain local.

Alternatives Considered:

### Single Shared Configuration

Pros:

- Simpler structure

Cons:

- User settings leak into source control

### Global User Configuration Only

Pros:

- Simpler local management

Cons:

- Impossible to customize behavior per checkout

Consequences:

Positive:

- Cleaner repositories
- Improved collaboration
- More flexible configuration

Negative:

- Multiple configuration files
- Additional migration considerations
