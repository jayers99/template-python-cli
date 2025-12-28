# ADR 001: Use Typer for CLI Framework

## Status

Accepted

## Context

We need a CLI framework for building Python command-line applications. The main options are:

1. **argparse** - Standard library, verbose, no type hints
2. **Click** - Mature, decorator-based, widely used
3. **Typer** - Built on Click, uses type hints, modern Python

## Decision

Use **Typer** as the CLI framework.

## Rationale

- **Type hints as configuration**: Function signatures define CLI arguments/options, reducing boilerplate
- **Built on Click**: Inherits Click's maturity and ecosystem while adding modern ergonomics
- **Automatic help generation**: Type hints generate accurate help text
- **Testing support**: `typer.testing.CliRunner` provides clean test interface
- **Consistent with Praxis patterns**: Matches the praxis-ai CLI implementation

## Consequences

### Positive

- Less boilerplate than argparse or raw Click
- Type checkers (mypy) validate CLI signatures
- Easy migration path to Click features when needed

### Negative

- Additional dependency beyond standard library
- Developers unfamiliar with Typer need to learn its conventions

## References

- [Typer documentation](https://typer.tiangolo.com/)
- [Click documentation](https://click.palletsprojects.com/)
