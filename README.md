# template-python-cli

A minimal Python CLI template following Praxis governance patterns.

## What's Included

- **Hexagonal architecture** -- `domain/` and `application/` layers
- **Typer CLI** -- type-hint-driven CLI framework
- **BDD testing** -- pytest-bdd with Gherkin feature files
- **Modern toolchain** -- uv, hatchling, ruff, mypy, just, pre-commit

## Quick Start

```bash
uv sync
just check
just test
```

## Customizing This Template

### 1. Rename the package

| Find                    | Replace With         |
|-------------------------|----------------------|
| `template-python-cli`   | `your-project-name`  |
| `template_python_cli`   | `your_package_name`  |
| `template-cli`          | `your-cli`           |

### 2. Update these files

- `pyproject.toml` -- name, description, authors, scripts entry
- `src/template_python_cli/` -- rename directory
- `tests/` -- update imports
- `README.md` -- replace this content

### 3. Verify

```bash
uv sync
just check
```

## Project Structure

```
src/your_package/
├── __init__.py        # Version
├── __main__.py        # python -m support
├── cli.py             # Typer CLI entry point
└── domain/
    └── greeter.py     # Business logic
tests/
├── conftest.py        # Shared fixtures
├── features/
│   └── cli.feature    # BDD scenarios
└── step_defs/
    └── test_cli.py    # Step definitions
```

## Task Runner

This project uses [just](https://github.com/casey/just) instead of Make.

```bash
just          # List all recipes
just sync     # Install dependencies
just test     # Run tests (accepts extra args: just test -k greet)
just lint     # Lint with ruff
just format   # Format with ruff
just typecheck # Type check with mypy
just check    # Run all checks
just clean    # Remove caches
```

Install: `brew install just`

## License

MIT
