# Template Python CLI -- Agent Notes

Minimal project template for scaffolding new Python CLI applications.

## Purpose

- **Code domain extension** providing scaffolding for new CLI projects
- Clone, rename, and start building

## Toolchain

- **Package manager:** uv
- **Build backend:** hatchling
- **Task runner:** just (justfile)
- **CLI framework:** Typer
- **Testing:** pytest + pytest-bdd (BDD with Gherkin)
- **Linting/formatting:** ruff
- **Type checking:** mypy (strict)
- **Git hooks:** pre-commit

## Key Files

| File | Purpose |
|------|---------|
| `src/template_python_cli/cli.py` | CLI entry point |
| `src/template_python_cli/domain/greeter.py` | Business logic |
| `tests/features/cli.feature` | BDD scenarios |
| `justfile` | Task runner recipes |

## When Working Here

- This is a **template**, not a running application
- Changes should be generic and reusable
- Keep example code minimal but demonstrative
