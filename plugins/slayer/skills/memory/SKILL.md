---
name: memory
description: Store reusable project decision rules, not temporary facts.
user-invocable: false
---

## Memory Rules

@${CLAUDE_PLUGIN_ROOT}/knowledge/memory-system.md

- Store rules that change future behavior.
- Do not store facts discoverable from current code.
- Prefer `.slayer/memory/long-term/` for stable project rules.
- Prefer `.slayer/memory/temp.md` for current-session lessons.
- Keep memory short and actionable.
