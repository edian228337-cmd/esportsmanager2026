# EMDB Studio Architecture

## Phase 1 Scope

Phase 1 establishes the architecture only. It intentionally avoids business logic, scraping behavior, database schema migrations, image processing, desktop UI behavior, and EMDB parsing algorithms.

## Architectural Style

EMDB Studio uses Clean Architecture with dependency inversion:

- **Core** owns generic contracts, base types, errors, and dependency injection primitives.
- **Provider adapters** (`hltv`, `liquipedia`) expose external data through interfaces and do not leak transport details.
- **Database** owns persistence boundaries.
- **Compiler** isolates all `.emdb` reverse-engineering and serialization concerns.
- **UI** will depend on application services instead of infrastructure details.

This layout keeps high-risk areas isolated: websites can change independently from the internal database, and `.emdb` reverse engineering can evolve without contaminating domain or UI code.

## Dependency Rule

Dependencies point inward:

```text
ui ─┐
services ───> core
hltv ───────> core
liquipedia ─> core
database ───> core
compiler ───> core
converter ──> core
images ─────> core
cache ──────> core
logos ──────> core
```

Infrastructure modules may implement core contracts. Core must not import infrastructure modules.

## Initial Folder Structure

```text
app/
  core/          Shared contracts, base classes, DI, and errors.
  config/        Application configuration primitives.
  database/      Persistence boundaries and future SQLite infrastructure.
  models/        Future domain models and DTOs.
  services/      Future use cases and orchestration services.
  hltv/          Future HLTV adapter implementation.
  liquipedia/    Future Liquipedia adapter implementation.
  compiler/      Isolated EMDB reader/parser/writer/compiler boundaries.
  converter/     Future mapping from internal DB to EMDB compiler inputs.
  cache/         Future HTTP and provider cache infrastructure.
  images/        Future image hashing/download/update service.
  logos/         Future logo-specific policies and storage helpers.
  ui/            Future PySide6 desktop application.
tests/           Test suite.
docs/            Architecture and decision records.
```

## Phase Dependency Graph

1. Architecture skeleton
2. Foundation infrastructure
3. HLTV adapter
4. Liquipedia adapter
5. Image manager
6. Internal SQLite database
7. Rating engine
8. EMDB reverse engineering
9. EMDB generator
10. Desktop application
11. Automatic updates

Each phase depends on the previous phases compiling and being tested before implementation continues.
