---
name: git-safety
description: Safe staged-diff, commit, branch, push, and release workflow.
user-invocable: false
---

@${CLAUDE_PLUGIN_ROOT}/knowledge/git-rules.md

## Git Safety Protocol

1. Orient: branch, status, remote.
2. Separate staged, unstaged, untracked, and ignored files.
3. Commit only staged or explicitly selected files.
4. Show message and scope before commit.
5. Push only after explicit approval for that exact push in the current task.
6. Approval to commit is not approval to push.
7. Show remote, branch, account if detectable, exact command, and scope before any approved remote write.
