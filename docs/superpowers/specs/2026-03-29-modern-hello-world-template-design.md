# Modern Hello World Template Design

**Date:** 2026-03-29
**Status:** Approved

## Goal

Strip template-python-cli down to a minimal, modern hello-world starting point. Easy to understand in under 5 minutes. Use as the reference pattern for migrating all other praxis-workspace Python projects from Poetry to uv.

## Structure

```
template-python-cli/
├── src/template_python_cli/
│   ├── __init__.py          # version string
│   ├── __main__.py          # python -m support
│   ├── cli.py               # Typer: hello command + --version
│   └── domain/
│       ├── __init__.py
│       └── greeter.py       # greet(name) -> str, validates input
├── tests/
│   ├── conftest.py          # CLI runner fixture
│   ├── features/
│   │   └── cli.feature      # 3 BDD scenarios
│   └── step_defs/
│       └── test_cli.py      # Step definitions
├── pyproject.toml            # uv + hatchling + ruff + mypy
├── justfile                  # Task runner (replaces Makefile)
├── .pre-commit-config.yaml
├── .gitignore
├── CLAUDE.md
├── README.md
└── LICENSE
```

## What's removed (vs current template)

- `infrastructure/` layer (config.py, console.py, logging.py)
- `docs/adr/` directory
- `info` and `config` CLI commands
- Rich and Pydantic as explicit dependencies (Typer bundles Rich)
- TOML config file system
- Environment variable integration
- Verbose/quiet flags
- Makefile (replaced by justfile)

## Dependencies

**Runtime:** `typer>=0.15.1` (single dependency)
**Dev:** `pytest`, `pytest-bdd`, `ruff`, `mypy`, `pre-commit`

## CLI

```
template-cli hello <name>   # Hello, <name>!
template-cli --version       # template-python-cli 0.1.0
```

## Domain layer

`greeter.py` — single function `greet(name: str) -> str` that validates the name is non-empty and returns the greeting. Raises `ValueError` on invalid input.

## Tests

3 BDD scenarios:
1. Show version
2. Greet a user
3. Empty name produces error

## justfile recipes

- `sync` — `uv sync`
- `test` — `uv run pytest` (accepts extra args)
- `lint` — `uv run ruff check .`
- `format` — `uv run ruff format . && ruff check --fix .`
- `typecheck` — `uv run mypy .`
- `check` — lint + typecheck + test
- `clean` — remove caches

## Toolchain

- **Package manager:** uv
- **Build backend:** hatchling
- **Linter/formatter:** ruff (E, F, I, UP, B, SIM)
- **Type checker:** mypy (strict)
- **Task runner:** just
- **Testing:** pytest + pytest-bdd
- **Git hooks:** pre-commit (ruff, mypy, trailing-whitespace)
