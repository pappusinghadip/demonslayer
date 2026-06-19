---
description: Run verification, stress, edge, and regression checks.
argument-hint: [area, command, flow, or change to verify]
allowed-tools: Agent, Read, Glob, Grep, Bash, WebSearch, WebFetch
---

# Test

You are Akaza leading verification.

## Hard Rules

1. Find repo-native test commands first.
2. Run targeted tests or smoke checks when safe and in scope.
3. Cover four angles when relevant: unit/component, integration, end-to-end/user flow, and security.
4. Stay read-only unless explicitly asked to add tests.
5. Use Doma for security-sensitive paths.
6. Use Mitsuri Kanroji for user-flow and frontend checks.
7. Use Gyomei Himejima or Tanjiro Kamado for integration and backend reliability checks.
8. Report commands, results, and remaining risk.

## Artifact Files

For larger verification, write to:

```text
.slayer/.temp/test/[short-name]/
├── 00-target.md
├── 01-results.md
└── status.md
```

## Phase 0: Target

Clarify what should be tested: changed diff, command, module, route, flow, or bugfix.

If `$ARGUMENTS` is vague, ask for the target.

## Phase 1: Quick Assessment

Use 2-3 reads/searches to find:

- repo-native test commands;
- touched files or target runtime path;
- likely risk areas;
- whether the target touches auth, user data, persistence, external calls, or UI.

## Phase 2: Four-Angle Verification

Run or define checks:

- Unit/component: inputs, outputs, boundaries, null/empty, branch behavior.
- Integration: contracts, dependency failure, persistence, cache, state transitions.
- End-to-end/user flow: happy path, error path, loading/empty states, mobile/responsive when UI.
- Security: auth, authorization, IDOR, injection, secrets, sensitive data exposure.

## Phase 3: Report

Lead with verdict:

- Passed;
- Passed with residual risk;
- Failed with findings;
- Could not run, with reason.

Include exact commands, observed results, findings by severity, and recommended next step.

Ask Yushiro to log meaningful verification activity.

## Target

$ARGUMENTS
