# Test Strategies

Use this for Akaza, Doma, Obanai Iguro, and lifecycle verification.

## Four-Angle Verification

| Angle | Owner | Focus |
|---|---|---|
| Unit or component | Akaza | Inputs, outputs, branches, nulls, empty values, boundaries |
| Integration | Akaza with Gyomei Himejima or Tanjiro Kamado | Contracts, dependencies, state transitions, failed services |
| End-to-end/user flow | Akaza with Mitsuri Kanroji | Real workflow, navigation, loading, empty, error, mobile states |
| Security | Doma | Auth, authorization, injection, IDOR, secrets, sensitive data |

## Priority

1. Critical user path.
2. Recently changed code.
3. Trust boundaries and persistence.
4. Error paths and failed dependencies.
5. Edge cases: null, empty, max/min, repeated action, race, timeout.

## Report Format

```text
SEVERITY: critical | high | medium | low
LOCATION: file:line or command
OBSERVED: what happened
EXPECTED: what should happen
IMPACT: user/system/security impact
RECOMMENDATION: focused fix or follow-up
```

## Stop Conditions

- Original bug or acceptance criteria verified.
- No critical/high findings remain, or user explicitly accepts them.
- Additional testing has diminishing returns and remaining risk is documented.
