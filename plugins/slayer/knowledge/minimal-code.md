# Minimal Code

Use this for every Slayer that writes or reviews code: Tanjiro, Mitsuri, Tamayo, Zenitsu, Gyomei, and Obanai.

The cleanest strike ends the fight in one motion. The best code is the code you never wrote.

## The Reuse Ladder

Before writing anything, climb this ladder and stop at the first rung that works:

1. Does this need to exist? If not, do not build it. Drop the requirement, not just the code.
2. Does the language standard library already do it? Use it.
3. Does the framework or platform already provide it? Use the native feature.
4. Is a dependency already installed that does it? Use what is there.
5. Can it be one line or one small function? Keep it that small.
6. Only then write the minimum that works and reads clearly.

## Rules

- Do not add a new dependency for what stdlib, the framework, or an installed package already covers. If a new dependency is genuinely needed, state why and ask first.
- No speculative abstraction. Do not add layers, wrappers, interfaces, config flags, or "future-proofing" for cases that do not exist yet. Solve today's requirement.
- Prefer removing code to adding code. Deleting a special case beats handling it.
- Inline over indirection until repetition forces a helper (rule of three).
- Match the existing pattern. Do not introduce a second way to do what the repo already does.
- One concern per change. A smaller diff is a faster review.

## The Floor — never cut these

Minimal means no waste, not no safety. Never trim:

- Input validation and error handling on real failure paths.
- Security controls: auth, output escaping, parameterized queries, secret handling.
- Required UI states (loading, empty, error) and accessibility.
- Tests for the behavior that changed.

## When Reviewing Or Planning

Flag over-engineering: unused abstraction, premature config, a dependency that duplicates stdlib, a wrapper with a single caller, dead options. Propose the smaller version and show what it removes.
