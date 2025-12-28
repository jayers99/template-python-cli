# ADR 002: Use Hexagonal Architecture

## Status

Accepted

## Context

We need a code organization strategy that:

- Separates business logic from infrastructure concerns
- Makes the codebase testable without external dependencies
- Scales as the application grows
- Provides clear boundaries for different concerns

## Decision

Use **Hexagonal Architecture** (Ports and Adapters) with three layers:

```
src/{package}/
├── domain/          # Core business logic, no external dependencies
├── application/     # Use cases, orchestration, service layer
└── infrastructure/  # External adapters (CLI, DB, APIs, file I/O)
```

## Rationale

- **Domain isolation**: Business rules don't depend on frameworks or I/O
- **Testability**: Domain and application layers can be unit tested without mocks
- **Flexibility**: Infrastructure can be swapped without touching core logic
- **Explicit dependencies**: Direction of imports enforces the architecture
- **Consistent with Praxis**: Matches praxis-ai's own structure

## Consequences

### Positive

- Clear separation of concerns
- Easy to test core logic in isolation
- Infrastructure changes don't ripple into business logic
- New developers understand where code belongs

### Negative

- More directories than a flat structure
- May feel like overkill for very simple CLIs
- Requires discipline to maintain layer boundaries

## Layer Guidelines

| Layer | Contains | Imports From |
|-------|----------|--------------|
| domain | Entities, value objects, domain services | (nothing external) |
| application | Use cases, orchestration | domain |
| infrastructure | CLI, repositories, external APIs | domain, application |

## References

- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [Ports and Adapters Pattern](https://herbertograca.com/2017/09/14/ports-adapters-architecture/)
