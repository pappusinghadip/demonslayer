# Security Checklist

Use this for Doma reviews.

- Authentication: missing checks, incorrect guard, token/session misuse.
- Authorization: IDOR, privilege escalation, role bypass.
- Input handling: SQL injection, shell injection, path traversal, XSS.
- Sensitive data: logs, API responses, secrets, keys, personal data leaks.
- State changes: CSRF, replay, race conditions, missing audit trail.
- File uploads: type bypass, path control, public exposure.

Report impact as what an attacker could do, not only what code looks wrong.
