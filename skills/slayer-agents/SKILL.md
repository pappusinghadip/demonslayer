---
name: slayer-agents
description: Private Slayers agent workflow for audit-first repo work, scoped fixes, review, testing, and git safety.
---

# Slayer Agents

Use this workflow when you want an audit-first development pass, natural Slayers routing, or a Claude Code plugin update.

## Local Claude Plugin

The Claude Code-style plugin lives at:

`plugins/slayer/`

Run locally with:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/slayer-agents/plugins/slayer
```

## Default Flow

1. Kagaya Ubuyashiki coordinates.
2. Audit the real runtime path before edits.
3. Use `/slayer:feature` for the full feature lifecycle.
4. Use `/slayer:bugfix` for the full bugfix lifecycle.
5. Use `/slayer:research`, `/slayer:explain`, or `/slayer:brainstorm` before planning when the problem is unclear.
6. Plan non-trivial changes when working manually.
7. Delegate scoped implementation to the right specialist.
8. Review with Obanai Iguro and security-check with Doma when relevant.
9. Verify with Akaza using unit/component, integration, end-to-end/user-flow, and security angles when relevant.
10. Use Tengen Uzui for staged diff, commit, PR, and release checks.
11. Use Yushiro for `.slayer/reports/`, `.slayer/memory/`, and artifact housekeeping.

## Natural Routing

Claude Code can route direct named requests:

```text
kagaya, build a search bar
akaza, test the auth flow
tengen, prepare the commit
```
