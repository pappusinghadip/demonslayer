---
name: verification
description: Verify behavior, tests, and remaining risk before calling work done.
user-invocable: false
---

@${CLAUDE_PLUGIN_ROOT}/knowledge/testing-checklist.md

## Completion Check

- Requirements addressed.
- Scope did not creep.
- Relevant tests or smoke checks ran.
- Security-sensitive paths reviewed when applicable.
- No debug logs, placeholders, or unrelated churn left behind.
- Any skipped verification is explicitly reported.
