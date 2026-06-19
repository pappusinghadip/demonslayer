# Memory System

Memory stores decision rules that change future behavior. It is not a cache of project facts.

## Files

```text
.slayer/memory/
├── temp.md
└── long-term/
    ├── index.md
    └── [category].md
```

## What Belongs In Memory

- Workflow rules learned the hard way.
- Repeated failure patterns.
- Project-specific verification commands or order.
- Agent routing lessons.
- Git and release constraints.

## What Does Not Belong

- Facts discoverable from current code.
- Full task progress.
- Raw test output.
- Temporary speculation.

## Write Format

Temporary:

```text
## YYYY-MM-DD HH:MM [agent] - [title]
[one or two line decision rule]
```

Long-term:

```text
## [decision rule title]
Learned: YYYY-MM-DD
Source: [command or agent]
Rule: [what to do or avoid]
Why: [brief reason]
```

Always update `.slayer/memory/long-term/index.md` after a long-term write.
