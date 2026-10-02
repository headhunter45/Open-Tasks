# ADR-0014 - Template Based Content Generation

Status:
Accepted

Context:

Work items, meetings, comments, and attachments require consistent initial structure.

Users should also be able to customize those structures.

Decision:

OT shall generate content from templates stored within the project.

Initial template categories include:

- Work items
- Meetings
- Shared templates

Default templates are installed during initialization.

Reasoning:

Templates allow projects to customize workflows without modifying OT source code.

Alternatives Considered:

### Hardcoded Templates

Pros:

- Simpler implementation

Cons:

- Difficult customization
- Requires OT modifications

### Global Templates

Pros:

- Easy user customization

Cons:

- Inconsistent repository behavior

Consequences:

Positive:

- Project-specific customization
- Reviewable template changes
- Consistent generation

Negative:

- Template migration complexity
- Additional validation requirements
