# PHP

Use this for PHP work: backend services, APIs, web apps, and framework code.
Apply only when the project uses PHP. If the project is not PHP, skip this file.

## Version Targeting

- Read the project floor from `composer.json` `require.php` before writing code. Never use a feature above that floor.
- Real spread here: some projects are PHP 7.4, others 8.0+. Match the project; do not assume latest.
- If the version is unclear, check `composer.json` or CI config, or ask. Do not guess.

| Feature | Min version |
|---|---|
| `declare(strict_types=1)`, typed properties, arrow `fn`, `??=` | 7.4 |
| Constructor promotion, union types, `match`, named args, nullsafe `?->` | 8.0 |
| Enums, `readonly` properties, first-class callable, `never` | 8.1 |
| `readonly` classes, DNF types | 8.2 |
| Typed class constants, `#[\Override]` | 8.3 |
| Property hooks, asymmetric visibility | 8.4 |

## Language Baseline

- Start every file with `declare(strict_types=1);` (works on 7.4+).
- Type everything the version allows: parameter, return, and property types. Union and `never` types need 8.0/8.1.
- Compare with `===`/`!==`. Never rely on loose `==` juggling.
- Avoid `eval`, `extract`, variable variables, and `@` suppression.

### On PHP 7.4

- Safe to use: typed properties, arrow functions `fn`, null coalescing assignment `??=`, array spread, return type declarations.
- Not available: constructor promotion, `match`, enums, `readonly`, union types, named arguments, nullsafe `?->`. Use classic equivalents (full constructors, `switch`, class constants, private properties with getters).

### On PHP 8.0+

- Prefer constructor promotion, `match`, named arguments, nullsafe `?->`, union types.
- On 8.1+ add enums, `readonly` properties, first-class callable `f(...)`.
- Adopt 8.2/8.3/8.4 features only when the project floor reaches that version.

## Style And Tooling

- Follow PER Coding Style 2.0; PSR-12 is fine for older projects. Enforce with `php-cs-fixer` or `phpcs`.
- PSR-4 autoloading via Composer. One class per file; namespace matches path.
- Static analysis: PHPStan or Psalm at the highest level the codebase passes. Set `phpVersion` to the project floor so it flags version-unsafe syntax. Treat new errors as blocking.
- Use Rector with the project's PHP version set as target; it will not introduce features above the floor.
- Tests: PHPUnit (9.x for 7.4, 10/11 for 8.1+) or Pest (8.x only). Name behavior, not methods.

## Clean Architecture

- Layer the code: Domain (entities, value objects, domain services) -> Application (use cases, DTOs) -> Infrastructure (DB, HTTP, framework) -> Presentation (controllers, CLI).
- Dependencies point inward. Domain depends on nothing framework-specific. No Eloquent/Doctrine/Request objects in the domain.
- Keep controllers thin: validate input, call a use case/action, return a response. No business logic in controllers.
- Use the repository pattern behind an interface defined in the domain; implement it in infrastructure.
- Map between layers with DTOs/value objects. Do not leak ORM models past the application boundary.
- Inject dependencies through the constructor; wire with the container, not service location.
- Prefer immutable value objects for money, ids, email, and similar. Use `readonly` on 8.1+; on 7.4 use private properties with no setters.

## Framework Notes

- Laravel: Form Requests for validation, Actions/Services for logic, API Resources for output, queued jobs for slow work, Eloquent only in the data layer.
- Symfony: Messenger bus for use cases, DTOs + Validator constraints, Doctrine repositories behind interfaces.
- Keep framework specifics at the edges so domain logic stays testable without booting the framework.

## Security (hand sensitive paths to Doma)

- Database access through PDO/ORM with bound parameters only. Never concatenate user input into SQL.
- Hash passwords with `password_hash` (bcrypt/argon2). Never MD5/SHA1.
- Escape output by context (HTML, attribute, JS, URL). Use template auto-escaping (`{{ }}`).
- Validate and whitelist input. Reject, do not silently sanitize.
- CSRF tokens on state-changing requests. Secure, HttpOnly, SameSite cookies.
- Keep secrets in env/secret store, never in code. Never log secrets, tokens, or PII.
