---
name: auto-init
description: Load project context, memory, and artifact state before Slayers lifecycle work.
user-invocable: false
---

## Project Context Check

Before larger work:

1. Check whether `.slayer/context/project.md` exists.
2. If missing, mention once that `/slayer:init` can create project context, then continue unless the user wants initialization first.
3. If present, read it silently and apply relevant runtime, test, and git notes.
4. If `.slayer/context/skills-registry.md` exists, read it when routing specialist work.

## Memory Check

Before planning, building, testing, or git operations:

1. Read `.slayer/memory/long-term/index.md` if it exists.
2. Read a detailed long-term memory file only when its index entry is relevant.
3. Read `.slayer/memory/temp.md` if it exists.
4. Apply memory quietly unless it changes the recommendation.

## Artifact Check

For lifecycle, research, debug, or test work:

1. Check `.slayer/.temp/` for matching in-progress work.
2. If a matching `status.md` exists, ask whether to resume or start fresh.
3. If starting fresh with a name collision, append a number to the directory.
4. Ensure `.slayer/.temp/` is ignored by git before creating artifacts.

## Activity Logging

After commands that produce meaningful work, ask Yushiro to append:

```text
YYYY-MM-DD HH:MM [command] [brief result] [files touched count if known]
```

to `.slayer/reports/activity.log`.
