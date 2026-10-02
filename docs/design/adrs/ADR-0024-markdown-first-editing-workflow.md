# ADR-0024 - Markdown First Editing Workflow

Status:
Accepted

Context:

Some project data is structured.

Some project data is narrative.

Users must be able to edit both.

Decision:

The primary editing experience shall be Markdown editing.

OT may provide convenience commands, but generated content must remain understandable and editable in standard text editors.

Reasoning:

The repository should remain usable without OT.

Markdown files should remain meaningful even when viewed directly in GitHub, GitLab, Obsidian, or a text editor.

Alternatives Considered:

### Structured Forms Only

Pros:

- Easier validation

Cons:

- Reduced transparency
- Requires OT for editing

### Database Editing

Pros:

- Strong data integrity

Cons:

- Incompatible with repository-native design

Consequences:

Positive:

- Tool independence
- Long-term portability
- Easier review

Negative:

- Parsing complexity
- Validation requirements
