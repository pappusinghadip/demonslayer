# CLAUDE.md

This repository defines a private Claude Code-style plugin named Slayer Agents.

## Architecture

- `plugins/slayer/agents/`: 10 public agent definitions plus internal Yushiro support.
- `plugins/slayer/commands/`: slash command prompts.
- `plugins/slayer/hooks/`: session-start context injection.
- `plugins/slayer/skills/`: reusable workflow skills.
- `plugins/slayer/knowledge/`: shared rules used by skills and agents.
- `.claude-plugin/marketplace.json`: Claude plugin marketplace metadata.
- `.codex-plugin/plugin.json`: local Codex plugin manifest.

## Rules

- Kagaya Ubuyashiki coordinates and plans. He does not directly edit source code.
- Yushiro owns activity logs, memory writes, reports, and artifact housekeeping only.
- Tengen Uzui owns git and release checks. He does not use broad staging commands.
- Obanai Iguro, Doma, and Akaza are read-only reviewers/testers.
- Source edits go through Tanjiro Kamado, Mitsuri Kanroji, Tamayo, Zenitsu Agatsuma, or Gyomei Himejima after approval.
- Audit and runtime-path tracing come before edits.
- Never use `git add .` in generated/noisy worktrees.
- Remote writes follow `Remote Write Safety` in `plugins/slayer/knowledge/core-principles.md`; do not duplicate or weaken that rule here.
- Keep generated workflow state under `.slayer/` or `.claude/slayer/`.
- Prefer natural routing skills for named requests: `kagaya`, `akaza`, and `tengen`.
- Keep `.slayer/.temp/` ignored before writing lifecycle artifacts.
