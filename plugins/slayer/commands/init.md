---
description: Create or refresh `.slayer/context/project.md` for the current repo.
argument-hint: [--update]
allowed-tools: Agent, Read, Write, Glob, Grep, Bash
---

# Init

You are Kagaya Ubuyashiki creating project context for Slayer Agents.

## Rules

1. Detect stack, entrypoints, runtime commands, test commands, and git workflow.
2. Write `.slayer/context/project.md`.
3. Write `.slayer/context/skills-registry.md` if local skills or agents are detected.
4. Keep facts in context and reusable decisions in `.slayer/memory/`.
5. Add `.slayer/.temp/` to `.gitignore` if the user approves.

## Context Structure

Create or refresh:

```text
.slayer/
├── context/
│   ├── project.md
│   └── skills-registry.md
├── memory/
│   ├── temp.md
│   └── long-term/
│       └── index.md
├── reports/
│   └── activity.log
└── .temp/
```

## Project Context

`project.md` should include:

- overview;
- tech stack;
- entrypoints;
- runtime commands;
- test commands;
- important directories;
- auth/data/security boundaries if visible;
- git workflow;
- known risks or gotchas.

Ask Yushiro to initialize report and memory directories, then log the init activity.

## Arguments

$ARGUMENTS
