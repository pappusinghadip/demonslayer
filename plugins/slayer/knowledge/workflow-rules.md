# Workflow Rules

## Audit First

- Start from the real runtime path: entrypoint, route, caller, config, backend file, database key, or staged diff.
- Do not answer from filename similarity alone.
- If several files look relevant, trace the active caller before concluding.

## Plan Before Edits

- For non-trivial changes, present a short plan and wait for approval.
- Include scope, files likely touched, verification, and rollback risk.
- If the user asked for audit only, do not edit.
- Approval is scoped to that plan. If scope, files, risk, or behavior changes, stop and ask again.

## Scope Discipline

- Preserve unrelated local edits.
- Search callers before changing public interfaces.
- Keep fixes narrow unless the user approves larger cleanup.
- Never hide uncertainty. Say what was verified and what is still assumed.

## Remote Write Safety

Follow `Remote Write Safety` in `core-principles.md`. Do not duplicate or weaken that rule here.

## Gate Handling

- If a gate is rejected, stop and do not advance the phase.
- Return to the prior phase needed to address the rejection.
- Update `status.md` with the rejected gate, reason, current phase, and next action.
- If tests or verification fail, report the failure, do not mark the task done, do not summarize as complete, and do not commit unless the user explicitly approves a follow-up fix or commit.
- After two failed fix/verification attempts, stop and escalate to the user.

## Artifact Paths

- Project context: `.slayer/context/project.md`
- Temporary work: `.slayer/.temp/`
- Memory: `.slayer/memory/`
- Reports: `.slayer/reports/`

## Artifact Discipline

- Before creating `.slayer/.temp/` artifacts, check whether `.slayer/.temp/`, `.slayer/`, or equivalent is gitignored.
- If not ignored, ask before appending `.slayer/.temp/` to `.gitignore`.
- Every lifecycle artifact directory should have `status.md`.
- `status.md` should include phase, status, summary, next action, and gate state.
- On resume, read `status.md` before continuing.
- Specialists should write details to artifact files and return short summaries.
- Do not write secrets, tokens, credentials, PII, or customer data into artifacts. Redact values and reference only locations.

## Activity Logging

- Use Yushiro for `.slayer/reports/activity.log`.
- Log meaningful lifecycle, research, test, review, commit, and PR work.
- Do not log invented token counts or unverified file counts.
