# Slayer Agents

Audit-first AI coding agents for Claude Code workflows.

Slayer Agents is a Claude Code-style plugin that gives you a small, opinionated squad of specialist agents for real software work: repo audits, scoped fixes, debugging, research, code review, verification, PR preparation, reporting, and git-safe delivery.

The roster is themed on Demon Slayer. The Demon Slayer Corps does the building, planning, and review; two demons — **Doma** and **Akaza** — form the adversarial red-team that hunts security holes and breaks weak code before users do. **Slayers build; demons break.** Every agent, demon or not, follows the same safety rules: read-only reviewers never mutate the worktree, secrets are never printed or logged, and nothing is pushed or published without explicit approval.

The workflow is simple:

1. Understand the real runtime path.
2. Plan before editing.
3. Make scoped changes.
4. Review and verify.
5. Commit only what was intended.

> Unofficial fan-themed project. This repository is not affiliated with, sponsored by, or endorsed by Koyoharu Gotouge, Shueisha, Aniplex, ufotable, or any related rights holder.

## Features

- Read-only audit command for tracing real code paths.
- Full gated feature lifecycle command for gather, research, plan, build, review plus test, and summary.
- Full gated bugfix lifecycle command for gather, investigate, fix plan, fix, verify, and summary.
- Planning command for implementation notes before edits.
- Research, explain, brainstorm, refactor, report, and PR commands.
- Scoped fix command for approved changes.
- Debug command for root-cause investigations.
- Review command with file and line findings.
- Test command for four-angle verification: unit/component, integration, E2E/user flow, and security.
- Commit command built around staged-diff safety.
- Project init command for generating local context.
- Natural routing skills for `kagaya`, `akaza`, and `tengen`.
- Yushiro internal support for activity logs, reports, memory, and artifact housekeeping.

## Agent Squad

| Agent | Role |
|---|---|
| Kagaya Ubuyashiki | Main orchestrator, planning, coordinates agents |
| Tanjiro Kamado | Implementation, architecture, automation, complex engineering |
| Mitsuri Kanroji | UI/UX, frontend, user flows |
| Tamayo | Deep debugging, unusual edge cases, hard investigations |
| Doma 🩸 | Security review, suspicious audit, auth and data leak checks (demon red-team) |
| Obanai Iguro | Code review, precise file and line findings |
| Akaza 🩸 | Stress testing, edge cases, performance pressure (demon red-team) |
| Zenitsu Agatsuma | Small scoped fixes, surgical changes |
| Gyomei Himejima | Data integrity, backend reliability, defensive design |
| Tengen Uzui | Git, release coordination, staged diff safety, final checklist |

Internal support:

| Agent | Role |
|---|---|
| Yushiro | Activity logging, reports, memory writes, artifact housekeeping |

## Installation

### Option 1: Install From GitHub In Claude Code

After this repository is available on GitHub:

```bash
/plugin marketplace add pappusinghadip/demonslayer
/plugin install slayer@slayer-agents
```

Then use the slash commands:

```text
/slayer:audit explain the auth flow
/slayer:feature add passkey login
/slayer:bugfix users cannot log in after password reset
/slayer:research auth flow
/slayer:explain checkout module
/slayer:plan add passkey login
/slayer:review staged changes
```

You can also use natural routing in Claude Code:

```text
kagaya, build a search bar
akaza, test the auth flow
tengen, prepare the commit
```

### Option 2: Run Locally From A Clone

Clone the repository:

```bash
git clone git@github.com:pappusinghadip/demonslayer.git
cd demonslayer
```

Run Claude Code with the plugin directory:

```bash
claude --plugin-dir "$PWD/plugins/slayer"
```

For the current local workspace:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/slayer-agents/plugins/slayer
```

## Quick Start

Initialize project context in any repo:

```text
/slayer:init
```

Audit before making changes:

```text
/slayer:audit why does /admin redirect to login
```

Create a plan before implementation:

```text
/slayer:plan add a manual passkey check after password login
```

Run a full feature lifecycle:

```text
/slayer:feature add a manual passkey check after password login
```

Run a full bugfix lifecycle:

```text
/slayer:bugfix login fails after password reset
```

Implement an approved scoped change:

```text
/slayer:fix implement the approved passkey plan
```

Review changed code:

```text
/slayer:review staged changes
```

Prepare a PR:

```text
/slayer:pr target main
```

Commit safely:

```text
/slayer:commit latest fix
```

## Commands

| Command | Purpose |
|---|---|
| `/slayer:audit` | Read-only repo audit and runtime path trace |
| `/slayer:brainstorm` | Compare options and tradeoffs before building |
| `/slayer:plan` | Create an implementation plan before editing |
| `/slayer:feature` | Gather -> research -> plan -> build -> review plus test -> summary |
| `/slayer:bugfix` | Gather -> investigate -> fix plan -> fix -> verify -> summary |
| `/slayer:fix` | Implement an approved scoped change |
| `/slayer:debug` | Root-cause debugging with approval before fixes |
| `/slayer:explain` | Layered codebase or feature explanation |
| `/slayer:research` | Deep read-only research from multiple angles |
| `/slayer:refactor` | Review-led refactoring with approval gate |
| `/slayer:review` | Code review and security-risk pass |
| `/slayer:test` | Four-angle verification, stress, and edge checks |
| `/slayer:commit` | Staged diff review and safe commit workflow |
| `/slayer:pr` | PR preparation with diff review and approval gate |
| `/slayer:report` | Activity summary from reports, memory, and artifacts |
| `/slayer:init` | Create project context for this workflow |

## Gated Lifecycles

Lifecycle state is written under `.slayer/.temp/`. If context is compacted or a terminal closes, restart by reading the task `status.md` and phase files. The commands check whether `.slayer/.temp/` is gitignored before writing artifacts.

### Feature Lifecycle

```text
/slayer:feature build a search bar

Phase 0  Gather         Requirements. Definition of done. Existing resources.
Phase 1  Research       Slayers explore the codebase from multiple angles in parallel.
          GATE          Confirm understanding before planning.
Phase 2  Plan           Architecture decisions, chunks, risks, and verification.
          GATE          Approve the plan before source edits.
Phase 3  Build          Slayers execute per the approved plan.
          GATE          Review what was built.
Phase 4  Review + Test  Obanai Iguro reviews. Doma audits sensitive paths. Akaza verifies from four angles.
          GATE          Decide which findings to fix, defer, or accept.
Phase 5  Summary        What was built, decisions made, test result, and reusable notes.
```

### Bugfix Lifecycle

```text
/slayer:bugfix users cannot log in after SSO

Phase 0  Gather         Bug details, logs, screenshots, impact, and timeline.
Phase 1  Investigate    Tamayo traces symptoms to root cause.
          GATE          Confirm the root cause before any fix is attempted.
Phase 2  Fix Plan       Proposed fix, blast radius, rollback, and verification.
          GATE          Approve the approach before source edits.
Phase 3  Fix            The right Slayer executes the fix.
          GATE          Review the fix.
Phase 4  Verify         Obanai Iguro reviews. Doma audits sensitive paths. Akaza confirms the bug is gone.
Phase 5  Summary        Root cause, fix, verification, and reusable decision rule.
```

Yushiro can log lifecycle output to `.slayer/reports/activity.log` and save reusable decision rules to `.slayer/memory/`.

## Recommended Workflow

### For New Features

```text
/slayer:feature build the new feature
/slayer:commit feature summary
```

### For Bugs

```text
/slayer:bugfix paste the error or describe the failing behavior
/slayer:commit bugfix summary
```

Use `/slayer:plan` plus `/slayer:fix` when you want to split the lifecycle manually. Use `/slayer:research`, `/slayer:explain`, or `/slayer:brainstorm` when you want understanding before any plan.

### For Git Handoff

```text
/slayer:review staged changes
/slayer:commit commit message or context
```

Tengen Uzui is intentionally staged-diff focused. The commit workflow should not use broad staging unless explicitly requested.

## How The Agents Route Work

- Kagaya Ubuyashiki coordinates larger work.
- Tanjiro Kamado handles complex implementation and automation.
- Mitsuri Kanroji handles frontend and user-facing flows.
- Tamayo handles difficult debugging.
- Gyomei Himejima handles backend reliability, persistence, and data safety.
- Zenitsu Agatsuma handles tiny low-risk patches.
- Obanai Iguro reviews code.
- Doma reviews security-sensitive paths.
- Akaza verifies edge cases, stress cases, and regressions.
- Tengen Uzui handles git, release checks, and final commit hygiene.
- Yushiro quietly handles `.slayer/` reports, memory, and activity logs.

## Repository Structure

```text
slayer-agents/
├── .claude-plugin/
│   └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── plugins/
│   └── slayer/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── agents/
│       ├── commands/
│       ├── hooks/
│       ├── knowledge/
│       └── skills/
├── scripts/
│   └── validate_slayer.py
├── skills/
│   └── slayer-agents/
│       └── SKILL.md
├── CLAUDE.md
└── README.md
```

## Validation

Run the structure validator:

```bash
python3 scripts/validate_slayer.py
```

Expected output:

```text
OK: Slayer Agents structure is valid
```

The validator checks:

- all 10 public agent files and internal Yushiro support agent exist;
- all command files exist;
- routing and shared-rule skills exist;
- hook files exist;
- required skills and knowledge files exist;
- agent skill references resolve;
- Claude plugin versions match;
- upstream reference identifiers are not present.

## Development

When editing the plugin:

1. Update agent, command, skill, or knowledge files under `plugins/slayer`.
2. Run validation.
3. Test locally with `claude --plugin-dir "$PWD/plugins/slayer"`.
4. Commit only intentional files.

Useful commands:

```bash
python3 scripts/validate_slayer.py
git status --short --branch
git diff --cached --name-status
```

## Git Safety Rules

Tengen Uzui follows these rules:

- start with `git status --short --branch`;
- inspect staged files with `git diff --cached --name-status`;
- inspect the actual staged diff before commit;
- never assume untracked files are included;
- never use `git add .` unless explicitly approved;
- remote writes follow `Remote Write Safety` in `plugins/slayer/knowledge/core-principles.md`;
- do not duplicate or weaken the core remote-write rule in command docs or agent docs.

## Generated State

Generated workflow state should stay out of normal commits:

```text
.slayer/.temp/
.claude/slayer/.temp/
```

Project context and memory may be created by `/slayer:init` inside a target repo.

## Versioning

Keep these versions in sync:

- `.claude-plugin/marketplace.json`
- `plugins/slayer/.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`

Run validation after version or metadata changes.

## License

No open-source license has been added yet. Unless a `LICENSE` file is added, all rights are reserved by the repository owner.
