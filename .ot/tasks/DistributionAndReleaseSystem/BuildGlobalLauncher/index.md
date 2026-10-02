---
id: 8f8bcc9c-4ebd-4bdf-a235-a1ed89c00acf
title: Build Global Launcher
type: feature
status: completed
size: medium
created_at: 2026-10-02T21:33:19.352468+00:00
parent: 29a5aa6d-eaac-4feb-bf1d-015003fd679b
author:
  name: Tom Hicks
  email: headhunter3@gmail.com
tags:
  - distribution
legacy_id: OT-034
---

## Description

Build Global Launcher in src/ot/launcher.py with project root resolution, configured version discovery, and delegation to project-installed binary (.ot/bin/ot.zipapp). Tested in tests/test_launcher.py.
