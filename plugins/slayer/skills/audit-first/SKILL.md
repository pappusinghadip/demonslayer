---
name: audit-first
description: Trace real runtime paths and evidence before edits or conclusions.
user-invocable: false
---

@${CLAUDE_PLUGIN_ROOT}/knowledge/workflow-rules.md

## Audit Protocol

1. Identify the active runtime path.
2. Read the caller and immediate callee.
3. Compare similarly named files before deciding which one is live.
4. Report evidence with file references.
5. Stop before edits unless the user approved implementation.
