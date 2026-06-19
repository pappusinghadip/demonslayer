# Android

Use this for Android work in Kotlin or Java: app modules, UI, data, and platform integration.
Apply only when the project targets Android. If it does not, skip this file.

## Language Baseline

- Kotlin-first. Write new code in Kotlin; treat Java as legacy to maintain or migrate.
- Prefer immutability: `val` over `var`, `data class`, read-only collections.
- Async with coroutines and Flow. Structured concurrency only: `viewModelScope`, `lifecycleScope`, injected dispatchers. Never `GlobalScope`.
- Model state and results with sealed classes/interfaces. Avoid nullable-as-state.
- Handle nullability explicitly. Avoid `!!`.

## Architecture (Google recommended)

- Three layers: UI (Compose + ViewModel) -> Domain (optional use cases) -> Data (repositories + data sources).
- Unidirectional data flow: events up, immutable UiState down.
- Single source of truth lives in the data layer. UI observes, never owns, the truth.
- ViewModel exposes `StateFlow<UiState>`; UI collects with `collectAsStateWithLifecycle()`.
- No Android framework types (Context, View, Activity) in domain or data logic.
- Pick one UI pattern and keep it consistent: MVVM or MVI.

## Clean Architecture

- Dependencies point inward: UI -> Domain -> Data interfaces. Domain has no Android, Retrofit, or Room imports.
- Repositories are interfaces at the domain/data boundary; implementations live in the data layer.
- Map DTO (network) and Entity (db) models to domain models. Do not expose Room/Retrofit models to the UI.
- Inject with Hilt. Constructor injection; scope correctly (`@Singleton`, `@ViewModelScoped`).
- Modularize as the app grows: `:core:*`, `:data:*`, `:feature:*`. Features do not depend on each other.

## Jetpack And Tooling

- UI: Jetpack Compose + Material 3. Keep composables stateless; hoist state. Use stable parameters and `derivedStateOf` to avoid needless recomposition.
- Persistence: Room for relational, DataStore for key-value. No SharedPreferences in new code.
- Navigation: Navigation Compose with type-safe routes.
- Background: WorkManager for deferrable work; coroutines for in-app async.
- Build: Gradle Kotlin DSL + version catalog (`libs.versions.toml`). Enable R8 for release.
- Tests: JUnit, Turbine for Flow, Compose UI tests, fakes over heavy mocks.

## Java (Legacy) Rules

- Use AndroidX, not the old support library.
- ViewBinding for views. No `findViewById`, no Kotlin synthetics.
- No `AsyncTask`. Use `Executors`/`ListenableFuture` or interop to coroutines.
- Migrate RxJava to coroutines/Flow incrementally, not in one sweep.
- New features should be Kotlin even in a Java codebase, unless the project forbids it.

## Security (hand sensitive paths to Doma)

- Do not store secrets/tokens in plaintext SharedPreferences or in code; use EncryptedDataStore/Keystore.
- Mark components `exported=false` unless they must be public; protect exported ones.
- Validate deep links and intent extras. Configure WebView safely (no unneeded JS, validate URLs).
- Use HTTPS with a network security config; never trust all certs.
