# Open Questions

This document tracks unresolved design questions for Open Tasks (ot).

Questions recorded here should eventually result in one of the following outcomes:

- Accepted architecture decision (ADR)
- Rejected architecture decision
- Design document clarification
- Removal if no longer relevant

Questions should remain here until a decision is documented elsewhere.

---

# OQ-0001 - Final Work Item Filesystem Layout

Status:
Open

Summary:

The final filesystem representation of a WorkItem has not been fully determined.

Current candidates include:

Option A:

```text
SomeTask.md
```

Option B:

```text
SomeTask/
  index.md
```

Option C:

```text
SomeTask.md
SomeTask/
```

Current Thinking:

Option B currently appears to be the preferred approach because it naturally supports:

- Attachments
- Child work items
- Future metadata

without special cases.

Related:

- ADR-0026 Work Item Filesystem Ownership

---

# OQ-0002 - Attachment Identifier Strategy

Status:
Open

Summary:

Attachments require stable identifiers.

Questions:

- Should attachments have UUIDs?
- Should attachments use task-local numbering?
- Should attachment identifiers incorporate task identifiers?
- Should attachment identifiers be globally unique?

Current Thinking:

Attachment identifiers appear useful for:

- References from comments
- References from descriptions
- Cross-referencing between work items

No identifier strategy has been selected.

---

# OQ-0003 - Attachment Metadata Model

Status:
Open

Summary:

Attachments may eventually require metadata beyond:

- Path
- URL
- Filename

Potential future requirements:

- Author
- Timestamp
- Attachment type
- External vs local indicator
- Description

Questions:

- Should attachments have dedicated metadata files?
- Should metadata live in the parent Markdown file?
- Should metadata be optional?

---

# OQ-0004 - Sprint Representation

Status:
Open

Summary:

Sprints have not yet been modeled.

Potential approaches:

Option A:

Represent sprints as WorkItems.

Option B:

Represent sprints as a dedicated model.

Questions:

- Do sprints require unique fields?
- Do sprints require unique validation?
- Do sprints require unique reporting?

Current Thinking:

A dedicated sprint model may be justified if sprint-specific metadata becomes significant.

---

# OQ-0005 - Meeting Storage Details

Status:
Open

Summary:

High-level meeting storage has been discussed.

Proposed structure:

```text
.ot/meetings/<meeting-type>/
```

Several implementation details remain unresolved.

Questions:

- Should active meetings be tracked separately?
- How should meeting attachments be organized?
- Should meetings contain structured metadata sections?
- Should meetings support child artifacts?

---

# OQ-0006 - Template Migration Behavior

Status:
Open

Summary:

User-modified templates must survive OT upgrades.

Questions:

- Should modified templates be preserved unchanged?
- Should modified templates be backed up and replaced?
- Should OT attempt template merging?
- Should template migration be interactive?

Current Thinking:

Automatic replacement of modified templates is undesirable.

---

# OQ-0007 - Configuration Schema Evolution

Status:
Open

Summary:

Configuration schema versioning has not been finalized.

Previous discussions introduced ideas such as:

```text
configSchemaVersion
configSchemaImplVersion
```

Questions:

- How many schema version values are required?
- Which values are user-visible?
- Which values are implementation details?
- How should migrations be represented?

---

# OQ-0008 - Work Item Short Identifier Implementation

Status:
Open

Summary:

The high-level identifier strategy has been decided.

The exact implementation has not.

Questions:

- Should short identifiers be derived directly from UUIDs?
- Should they be derived from hashes of UUIDs?
- What minimum display length should be used?
- What minimum accepted user prefix should be accepted?

Current Thinking:

Git-style shortest unique prefix behavior remains the preferred direction.

---

# OQ-0009 - Work Item Relationship Representation

Status:
Open

Summary:

Parent-child and dependency relationships are currently expected to be explicit.

The precise storage format is not yet finalized.

Questions:

- Store parent references only?
- Store parent and child references?
- Store dependency references bi-directionally?
- Store relationships in metadata or generated sections?

---

# OQ-0010 - Monotonic Numeric Identifier Removal

Status:
Open

Summary:

Older designs included:

```text
system.next_id_number
ot id next
ot id next --claim
```

UUIDs have largely replaced this design.

Questions:

- Is a monotonic identifier still needed?
- Should numeric identifiers remain as optional user-facing values?
- Can the counter be removed entirely?

Current Thinking:

The counter may eventually be removed.

---

# OQ-0011 - Active Meeting Tracking

Status:
Open

Summary:

Multiple commands imply awareness of meetings currently in progress.

Examples:

```text
ot meeting start
ot meeting end
ot meeting list
```

Questions:

- How should active meetings be tracked?
- Can multiple active meetings exist?
- Should active meetings be represented through filesystem state?
- Should OT maintain a session file?

---

# OQ-0012 - Work Item Display Naming

Status:
Open

Summary:

Work items currently use filenames as human-readable identifiers.

Questions:

- Should filenames be generated from titles?
- Should filenames remain stable after renaming?
- Should filenames include identifiers?
- Should filenames be freely editable?

---

# OQ-0013 - Validation Scope

Status:
Open

Summary:

OT intends to validate repository consistency.

Questions:

- Should validation include only OT-managed files?
- Should validation inspect links outside .ot?
- Should validation attempt to verify external attachment URLs?
- Should validation detect orphaned assets?

---

# OQ-0014 - Global OT Cache Structure

Status:
Open

Summary:

Global OT storage has been proposed:

```text
~/.ot/
```

Potential contents:

```text
config.json
cache/
versions/
```

Questions:

- How should downloaded versions be cached?
- Should caches be shared across projects?
- How should cache cleanup work?

---

# OQ-0015 - Future Version Control Support

Status:
Open

Summary:

Git support is the primary goal.

Mercurial support is desirable.

Questions:

- What abstraction layer should be used?
- What functionality must every supported VCS provide?
- How should unsupported systems behave?

Current Thinking:

Unsupported version control systems should behave the same as no version control.

Related:

- ADR-0004 Version Control Optional
- ADR-0005 Git Preferred Integration

---

# OQ-0016 - Repository Layout Overrides

Status:
Open

Summary:

Current plans allow users to relocate many OT folders through configuration.

Questions:

- Which paths should be configurable?
- Which paths should remain fixed?
- Can .ot itself be relocated?
- Should templates and meetings support independent relocation?

Current Thinking:

.bin and configuration are likely to remain fixed while most content folders remain configurable.

---

# OQ-0017 - Attachment Ownership Rules

Status:
Open

Summary:

Attachment cleanup and validation require ownership rules.

Questions:

- Can attachments belong to multiple work items?
- How should shared attachments be represented?
- When should fix recommend moving an attachment?
- When should fix recommend deleting an attachment?

---

# OQ-0018 - Future Plugin and Extension Model

Status:
Open

Summary:

No plugin system currently exists.

Questions:

- Will OT ever support plugins?
- Is template customization sufficient?
- Should import/export tools be considered extensions?

Current Thinking:

Template customization is preferred over code customization whenever practical.
