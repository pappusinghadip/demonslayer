# Testing Checklist

Use this for Akaza and verification tasks.

- Find the repo-native test command before inventing one.
- If no test framework exists, use targeted smoke checks and static review.
- Cover four angles when relevant: unit/component, integration, end-to-end/user flow, and security.
- Cover happy path, empty/null, boundary values, failed dependency, and permission failure.
- For frontend, check loading, empty, error, and mobile/responsive states.
- For backend, check API contract, status/body, persistence, cache invalidation, and logs.
- For auth or user data, ask Doma for a security pass.
- Report exact commands run and whether they passed.
