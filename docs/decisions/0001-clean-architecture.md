# ADR 0001: Use Clean Architecture Boundaries

## Status

Accepted for Phase 1.

## Context

EMDB Studio must combine volatile external sources, a normalized internal
SQLite database, generated binary assets, reverse-engineered `.emdb` files, and
a desktop UI. These responsibilities change at different rates and should not be
coupled directly.

## Decision

Use Clean Architecture boundaries with dependency inversion. Core contracts are
kept provider-neutral. Infrastructure adapters implement those contracts in
later phases. The EMDB compiler remains isolated behind `compiler/` boundaries.

## Consequences

- Provider changes should not force UI or compiler changes.
- Reverse-engineering experiments remain isolated from normalized data and UI.
- Early phases can be tested with contracts before external integrations exist.
- More files are created up front, but each file has a narrow responsibility.
