# ADR-0002 - Markdown as Primary Storage Format

Status:
Accepted

Context:

OT requires a storage format for user-editable information such as:

- Work item descriptions
- Meeting notes
- Planning artifacts
- Comments

The format should be easy for both humans and tools to consume.

Decision:

Use Markdown as the primary storage format for user-editable content.

Reasoning:

Markdown is:

- Human readable
- Plain text
- Widely supported
- Easy to review in pull requests
- Easy to search
- Easy to edit manually
- Compatible with GitHub
- Compatible with GitLab
- Compatible with Obsidian

Users should be able to inspect and modify project data without requiring OT.

Alternatives Considered:

### JSON

Pros:

- Structured
- Easy to parse

Cons:

- Poor long-form authoring experience
- Difficult manual editing

### YAML

Pros:

- Human readable
- Structured

Cons:

- Error-prone indentation
- Less friendly for long-form content

### Database Storage

Pros:

- Structured
- Efficient queries

Cons:

- Not directly editable
- Requires tooling

Consequences:

Positive:

- Easy review process
- Tool independence
- Human-readable history
- Strong ecosystem support

Negative:

- Requires validation
- Requires parsing conventions
- Some structured data may require frontmatter or metadata blocks
