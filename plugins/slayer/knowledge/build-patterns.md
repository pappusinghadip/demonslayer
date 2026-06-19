# Build Patterns

Use this for Kagaya Ubuyashiki and implementation agents.

## Decomposition

Parallelize only when chunks are genuinely independent:

- Parallel dispatch is allowed only for non-overlapping file sets.
- UI and backend can run in parallel if they touch separate files and share a clear contract.
- Multiple unrelated bug fixes can run in parallel.
- Research angles can run in parallel.
- If two agents may touch the same file, run sequentially or isolate work in separate worktrees.

Sequence work when there is a dependency:

- Schema or model change before API/UI updates.
- Shared interface change before callers.
- Config or generated code before build verification.
- Same file edits should usually be owned by one agent.

## Agent Selection

| Work | Agent |
|---|---|
| Architecture, services, automation, complex implementation | Tanjiro Kamado |
| UI, UX, frontend flows, responsive behavior | Mitsuri Kanroji |
| Root-cause debugging and strange failures | Tamayo |
| Small safe patch | Zenitsu Agatsuma |
| Data, persistence, migrations, caches, backend invariants | Gyomei Himejima |
| Security review | Doma |
| Code review | Obanai Iguro |
| Stress, edge, performance, regression verification | Akaza |
| Git, PR, release, staged diff safety | Tengen Uzui |

## Conflict Resolution

1. Stop if two agents need to edit the same file.
2. Assign one owner for that file.
3. Run sequentially, or isolate work in separate worktrees when true parallelism is required.
4. Re-read the final diff before review.
5. If a change grew beyond approved scope, ask the user.

## Build Output Discipline

Each builder reports:

- files changed;
- decisions made;
- assumptions;
- verification run or skipped;
- remaining risk.
