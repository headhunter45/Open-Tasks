---
id: 33333333-3333-4333-8333-333333333333
title: Fix Login Crash on Null Password
type: bug
status: triage
size: small
created_at: 2026-10-02T08:00:00Z
dependencies:
  - 22222222-2222-4222-8222-222222222222
author:
  name: Charlie Brown
  email: charlie@example.com
tags:
  - bugfix
  - crash
---

# Fix Login Crash on Null Password

## Steps to Reproduce

1. Open login dialog.
2. Submit form with empty/null password string.
3. Observe unhandled exception in authentication handler.

## Expected Behavior

Return an input validation error message rather than raising an unhandled exception.
