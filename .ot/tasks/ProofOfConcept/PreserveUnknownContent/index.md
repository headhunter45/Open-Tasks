---
id: a09fdca2-a3ad-4ff8-a802-c46e167ef687
title: Preserve Unknown Content
type: feature
status: completed
size: medium
created_at: 2026-10-02T21:33:19.347616+00:00
parent: 3c8864d8-c2da-4e13-9c5c-33c2a3267d88
author:
  name: Tom Hicks
  email: headhunter3@gmail.com
tags:
  - poc
legacy_id: OT-019
---

## Description

Preserve unknown user-defined markdown sections, frontmatter fields, and custom content without destructive reformatting during parse-and-write cycles. Implemented in src/ot/parser.py and tested in tests/test_parser.py.
