# ADR-0022 - Template Customization Over Code Customization

Status:
Accepted

Context:

Different teams often require different:

- Work item formats
- Meeting formats
- Comment structures

These differences should not require changes to OT source code.

Decision:

Projects should customize content generation through templates whenever possible.

OT features should not be added solely to support formatting preferences.

Reasoning:

Templates allow teams to adapt output while preserving a common implementation.

Alternatives Considered:

### Hardcoded Formats

Pros:

- Simple implementation

Cons:

- Inflexible

### Plugin-Based Formatting

Pros:

- Flexible

Cons:

- Increased complexity
- Larger maintenance burden

Consequences:

Positive:

- Easier customization
- Reduced feature pressure
- Simpler core design

Negative:

- More responsibility on template authors
