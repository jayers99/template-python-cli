# Template Python CLI — Agent Notes

This is a **project template** for scaffolding new Python CLI applications.

## Purpose

- **Code domain extension** providing scaffolding for new CLI projects
- Used via `praxis extensions add template-python-cli` or as a GitHub template

## What It Provides

- Hexagonal architecture (`domain/`, `application/`, `infrastructure/`)
- Typer CLI framework with production patterns
- BDD testing (pytest-bdd + Gherkin)
- Quality tooling (ruff, mypy, pre-commit)
- Poetry packaging

## Key Files

| File | Purpose |
|------|---------|
| `src/template_python_cli/cli.py` | CLI entry point |
| `src/template_python_cli/domain/` | Business logic |
| `tests/features/` | Gherkin feature files |
| `docs/adr/` | Architecture decisions |

## When Working Here

- This is a **template**, not a running application
- Changes should be generic/reusable patterns
- Keep example code minimal but demonstrative
- Update README customization checklist when adding features
