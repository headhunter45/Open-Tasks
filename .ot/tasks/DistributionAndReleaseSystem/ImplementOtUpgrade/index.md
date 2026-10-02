---
id: 7c5b027c-2409-4cc5-8cae-90f5e31a6ab5
title: Implement ot upgrade
type: feature
status: completed
size: medium
created_at: 2026-10-02T21:33:19.354346+00:00
parent: 29a5aa6d-eaac-4feb-bf1d-015003fd679b
author:
  name: Tom Hicks
  email: headhunter3@gmail.com
tags:
  - distribution
legacy_id: OT-041
---

## Description

Implement 'ot upgrade' CLI command supporting --version <v>, --mirror <dir>, and --dry-run flags for automated project upgrades. Implemented in src/ot/cli.py, src/ot/upgrade.py, and tested in tests/test_upgrade.py.
