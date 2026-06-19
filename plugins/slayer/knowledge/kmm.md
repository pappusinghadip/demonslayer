# Kotlin Multiplatform (KMM/KMP)

Use this for Kotlin Multiplatform work: shared business logic across Android and iOS.
Apply only when the project has a shared Kotlin Multiplatform module. If not, skip this file.

## Source Set Discipline

- `commonMain` holds platform-agnostic code only. No Android (`android.*`), no iOS, no JVM-only APIs.
- Platform code lives in `androidMain` / `iosMain` and fulfills `expect` declarations with `actual`.
- The iron rule: if a type is platform-specific, it does not belong in `commonMain`. Abstract it behind an interface or `expect`.
- Keep `expect/actual` surfaces small. Prefer interfaces + DI over large `expect` classes.

## What To Share

- Share the domain and data layers: models, use cases, repositories, validation, networking, serialization, persistence.
- Keep UI native per platform (Compose on Android, SwiftUI on iOS), or use Compose Multiplatform only if the project commits to it.
- Shared ViewModels are allowed via the multiplatform `androidx.lifecycle` ViewModel.

## Clean Architecture

- Domain (entities, use cases, repository interfaces) in `commonMain`, free of platform or library leakage.
- Data implementations (Ktor, SQLDelight) in `commonMain` where the library is multiplatform; platform-only pieces drop to `androidMain`/`iosMain` behind interfaces.
- Dependency inversion across the platform boundary: common defines interfaces, platforms provide `actual` implementations.
- Map transport/platform models to domain models inside the shared layer. Do not leak DTOs to platform UI.

## Libraries And Tooling

- Networking: Ktor client. Serialization: kotlinx.serialization. DB: SQLDelight. Time: kotlinx.datetime. Concurrency: kotlinx.coroutines. DI: Koin or manual.
- Settings/preferences: multiplatform-settings.
- Expose suspend functions and `Flow` to iOS carefully; wrap with SKIE or a Flow adapter so Swift gets ergonomic, cancellable APIs.
- Keep targets in the version catalog and declare them explicitly (`androidTarget()`, iOS targets).

## Pitfalls

- Do not block on coroutines to satisfy a platform API; provide proper async wrappers.
- Watch iOS threading when exposing shared state; prefer immutable data crossing the boundary.
- Avoid `expect` on data classes; prefer common interfaces with platform `actual` factories.
