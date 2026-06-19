# Design Routing

Use this for Mitsuri Kanroji and Kagaya Ubuyashiki on visual, UI, or design-system work.
Apply only when the task involves design, look-and-feel, layout, or visual QA.

## Principle

Slayers builds and verifies; it does not invent a visual system from scratch when a
specialist design skill is available. Before hand-crafting design, check for an installed
design skill that does the job better and invoke it. Hand-build only when none is present.

## Routing Matrix

Match the design intent to the best available skill. Invoke it if installed in this
session; otherwise use the fallback.

| Design intent | Prefer skill (if installed) | Fallback if not installed |
|---|---|---|
| New product, no design system or brand | `design-consultation` (creates `DESIGN.md`) | Define tokens inline: type scale, spacing, color, radius |
| Explore several visual directions | `design-shotgun` (variants + compare board) | Sketch 2-3 options in code, pick with the user |
| Turn an approved design into HTML/CSS | `design-html` | Build with the existing component library |
| Visual QA on a live page (spacing, hierarchy, slop) | `design-review` | Self-check against the hand-build principles |
| Design review inside a plan, pre-build | `plan-design-review` | Note design risks in the plan |
| General frontend design or polish | `frontend-design`, `ui-ux-pro-max` | Hand-build per principles below |

## How To Route

1. Read `DESIGN.md` or the project design system first if it exists. Obey its tokens.
2. Identify the design intent in the matrix above.
3. If a matching skill is installed, invoke it (Mitsuri Kanroji via the Skill tool; Captain
   America via Skill or by dispatching) and build against its output.
4. Confirm with the user before invoking heavy or interactive skills (`design-shotgun`,
   `design-consultation`). Invoke lightweight help and QA (`frontend-design`,
   `design-review`) directly.
5. If no design skill is installed, hand-build with the principles below and say so.
6. Never freestyle a new visual system when `design-consultation` or `DESIGN.md` applies.

## Hand-Build Principles (fallback)

- Reuse existing components and tokens. Do not introduce a parallel style.
- One type scale, one spacing scale (4/8px rhythm), one color system. No magic numbers.
- Respect responsive breakpoints; design mobile and desktop; cover empty, loading, and error states.
- Accessibility: semantic markup, focus states, contrast, hit targets, labels.
- Avoid AI-slop: random gradients, inconsistent spacing, center-everything, emoji bullets.
- Hand visual-system decisions and final visual QA to a design skill when one exists.
