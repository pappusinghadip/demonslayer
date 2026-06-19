# Git Rules

Use this for Tengen Uzui.

- Start with `git status --short --branch`.
- Inspect staged changes with `git diff --cached --name-status` and `git diff --cached`.
- Do not assume untracked files are included.
- Do not use `git add .` unless the user explicitly approves the full worktree.
- Preserve unrelated local edits.
- Remote writes follow `Remote Write Safety` in `core-principles.md`. Do not duplicate or weaken that rule here.
- After push/merge claims, verify the actual command result and current branch.
- For PR work, detect the platform from `git remote -v` before suggesting `gh`, `glab`, or manual PR steps.
- If `gh auth status` or another CLI account does not match the remote owner, warn before publishing.
