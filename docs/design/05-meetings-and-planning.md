# Meetings and Planning

## Overview

This document describes how Open Tasks (ot) models planning activities, meetings, and related artifacts.

OT treats planning artifacts as repository content rather than transient application state.

Meeting records are intended to be:

- Human readable
- Reviewable
- Version controlled
- Auditable
- Directly editable

Meeting records are considered first-class project artifacts.

Related:

- ADR-0020 Pull Requests as Review Authority
- ADR-0021 Meeting Verification Through Repository Review
- ADR-0024 Markdown First Editing Workflow

---

# Goals

The meeting system should support:

- Backlog grooming
- Sprint planning
- Sprint retrospectives
- Idea exploration
- Project coordination
- Historical auditing

The system should not attempt to replace real-time meeting platforms.

OT records meeting outcomes rather than hosting meetings.

---

# Philosophy

## Meetings Are Project Artifacts

A meeting represents a decision-making activity that affects project planning.

Examples:

- Creating tasks
- Updating statuses
- Grooming backlog items
- Clarifying requirements
- Changing priorities

The resulting record is part of the project history.

---

## Meetings As Source Code

Meeting outcomes should be reviewable in the same manner as source code.

Meeting notes:

- Live in the repository
- Participate in pull requests
- Participate in review workflows
- Participate in auditing workflows

Meeting records should remain useful even without OT.

---

## Repository Review Is Verification

OT does not maintain a separate meeting approval system.

Meeting verification should occur through repository review processes.

Examples:

- Pull request reviews
- Pull request approvals
- Repository history

See:

- ADR-0021 Meeting Verification Through Repository Review

---

# Meeting Types

Meeting types are configurable.

Valid meeting types are defined through:

```text
meeting.types
```

Example meeting types:

```text
grooming
planning
retrospective
ideation
```

Projects may introduce additional types.

See:

- 03-configuration-system.md

---

# Backlog Grooming Meetings

## Purpose

Backlog grooming meetings are used to:

- Review newly created work items
- Clarify requirements
- Refine descriptions
- Estimate effort
- Assign sizes
- Assign priorities
- Split oversized work

---

## Typical Outcomes

Examples:

```text
Status Changes
Description Updates
New Child Work Items
Dependency Changes
Size Assignments
```

---

# Sprint Planning Meetings

## Purpose

Sprint planning meetings determine:

- Work to be included in a sprint
- Sprint priorities
- Team commitments
- Scheduling decisions

---

## Typical Outcomes

Examples:

```text
Sprint Assignment
Priority Changes
Task Selection
Dependency Identification
```

---

# Sprint Retrospectives

## Purpose

Retrospectives evaluate completed work.

Topics may include:

- Successes
- Areas for improvement
- Process changes
- Action items

---

## Typical Outcomes

Examples:

```text
Process Improvements
Follow-Up Work Items
Lessons Learned
```

---

# Ideation Meetings

## Purpose

Ideation meetings focus on poorly defined work.

Examples:

```text
New Features
Research Topics
Large Epics
Product Ideas
```

---

## Typical Outcomes

Examples:

```text
Requirements Discovery
New Work Items
Technical Spikes
Design Exploration
```

---

# Meeting Lifecycle

## Meeting Start

Meetings begin using:

```text
ot meeting start
```

Example:

```bash
ot meeting start --type grooming
```

The command creates a new meeting document using the appropriate meeting template.

Expected actions:

- Determine meeting type
- Create meeting document
- Assign timestamp
- Initialize meeting metadata

Template selection is based on:

```text
meeting.types
```

and project templates.

---

## Meeting Activity

During a meeting, users may:

- Edit the meeting record
- Edit WorkItems
- Add comments
- Add attachments
- Create new WorkItems

OT does not attempt to control how users conduct the meeting itself.

The meeting record serves as a planning artifact and audit record.

---

## Meeting End

Meetings end using:

```bash
ot meeting end
```

Expected actions:

- Mark meeting as ended
- Record ending timestamp
- Validate meeting state
- Remind the user to review and publish changes

Future enhancements may include:

- Reviewer checklist generation
- Attendee verification reminders
- Meeting summary generation

---

# Meeting Records

## Storage

Current preferred location:

```text
.ot/meetings/<meeting-type>/
```

Example:

```text
.ot/meetings/grooming/
```

Meeting storage details remain under discussion.

See:

- OQ-0005 Meeting Storage Details

---

## Naming

The current preferred approach is timestamp-based naming.

Example:

```text
2026-08-12T09-00-00.md
```

Alternative naming schemes may be evaluated in the future.

---

# Meeting Metadata

Meeting records are expected to contain metadata such as:

```text
Meeting Type
Creation Timestamp
End Timestamp
Organizer
Attendees
```

The exact metadata format remains flexible.

---

# Attendees

Meetings may track attendees.

Potential attendee information:

```text
Name
Email Address
Username
```

Attendee representation has not been finalized.

Current expectation is that attendee information remains human readable.

---

# Meeting Notes

Meeting notes are expected to be written in Markdown.

Notes should remain understandable when viewed through:

- GitHub
- GitLab
- Obsidian
- Text editors

No OT-specific tooling should be required to read notes.

---

# Related Work Items

Meeting records may reference WorkItems.

Examples:

```text
Items Groomed
Items Created
Items Updated
Items Discussed
```

References should use WorkItem identifiers.

See:

- 04-work-item-model.md

---

# Meeting Attachments

Meetings may contain attachments.

Examples:

```text
Diagrams
Images
Documents
Research
```

The exact attachment structure remains under discussion.

See:

- OQ-0005 Meeting Storage Details

---

# Planning Workflows

## Creating Work During Meetings

Meetings frequently create new WorkItems.

Examples:

```text
New Bugs
New Enhancements
New Epics
New Tasks
```

OT should make this process straightforward.

WorkItems created during meetings become normal WorkItems and follow normal validation rules.

---

## Updating Existing Work

Meetings frequently modify existing WorkItems.

Examples:

```text
Status Updates
Size Changes
Dependency Updates
Requirement Clarification
```

All modifications should be reviewable through normal repository workflows.

---

# Pull Request Workflow

The preferred workflow is:

```text
Start Meeting
    ↓
Edit Work Items
    ↓
Edit Meeting Record
    ↓
End Meeting
    ↓
Create Pull Request
    ↓
Review
    ↓
Merge
```

Meeting approval occurs through repository review rather than a dedicated approval system.

---

# Validation

Meeting validation may include:

- Valid meeting type
- Required metadata
- Valid WorkItem references
- Valid attachments
- Timestamp consistency

Validation is performed through:

```text
ot check
ot check --fix
```

---

# Active Meetings

OT may support tracking currently active meetings.

Potential commands:

```text
ot meeting list
```

The implementation remains under discussion.

Questions include:

- Can multiple meetings be active?
- How is active state recorded?
- How is interrupted work handled?

See:

- OQ-0011 Active Meeting Tracking

---

# Sprints

Sprint representation remains an open question.

Potential approaches:

- Sprint as WorkItem
- Dedicated Sprint model

See:

- OQ-0004 Sprint Representation

No final sprint implementation has been selected.

---

# Future Features

Potential future additions include:

- Sprint reports
- Meeting summaries
- Burndown reporting
- Capacity planning
- Agenda generation
- WorkItem recommendation

These features must remain consistent with OT's repository-native philosophy.

---

# Open Questions

The following planning topics remain unresolved:

- OQ-0004 Sprint Representation
- OQ-0005 Meeting Storage Details
- OQ-0011 Active Meeting Tracking

Additional planning and meeting functionality
