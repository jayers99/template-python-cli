# template-python-cli

A Python CLI project template following Praxis governance patterns.

## What's Included

- **Hexagonal architecture** - `domain/`, `application/`, `infrastructure/` layers
- **Typer CLI framework** - Modern, type-hint-based CLI
- **BDD testing** - pytest-bdd with Gherkin feature files
- **Quality tools** - ruff (linting), mypy (type checking)
- **Pre-commit hooks** - Automated code quality checks
- **Poetry packaging** - Dependency management and packaging

## Quick Start

1. Use this template to create a new repository
2. Clone your new repository
3. Follow the customization checklist below
4. Run `poetry install`

---

## Customizing This Template

### Step 1: Rename the Package

Replace `template_python_cli` with your package name throughout the project.

**Search and replace:**

| Find | Replace With |
|------|--------------|
| `template-python-cli` | `your-project-name` |
| `template_python_cli` | `your_package_name` |

**Files to update:**

- [ ] `pyproject.toml` - project name, package path, script entry point
- [ ] `src/template_python_cli/` - rename directory
- [ ] `tests/` - update imports

### Step 2: Update pyproject.toml

```toml
[tool.poetry]
name = "your-project-name"          # Your project name
version = "0.1.0"
description = "Your description"
authors = ["Your Name <you@example.com>"]

[tool.poetry.packages]
include = "your_package_name"
from = "src"

[tool.poetry.scripts]
your-cli = "your_package_name.cli:app"    # CLI command name
```

### Step 3: Update Metadata

- [ ] `README.md` - Replace this content with your project docs
- [ ] `LICENSE` - Update copyright holder if needed
- [ ] `pyproject.toml` - Add your description, authors, repository URL

### Step 4: Verify Setup

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run linting
poetry run ruff check .

# Run type checking
poetry run mypy .

# Test CLI
poetry run your-cli --help
```

---

## Project Structure

```
your-project/
├── src/your_package/
│   ├── __init__.py
│   ├── __main__.py           # python -m support
│   ├── cli.py                # Typer CLI entry point
│   ├── domain/               # Core business logic
│   ├── application/          # Use cases, services
│   └── infrastructure/       # External adapters
├── tests/
│   ├── features/             # Gherkin feature files
│   ├── step_defs/            # BDD step definitions
│   └── conftest.py           # Shared fixtures
├── docs/
│   └── adr/                  # Architecture Decision Records
├── pyproject.toml
└── README.md
```

## Pre-commit Hooks

This template includes pre-commit hooks for automated code quality checks.

**Setup:**

```bash
# Install pre-commit
pip install pre-commit

# Install hooks (runs automatically on git commit)
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

**Included hooks:**

- **ruff** - Linting and auto-fix
- **ruff-format** - Code formatting
- **mypy** - Type checking
- **trailing-whitespace** - Remove trailing whitespace
- **end-of-file-fixer** - Ensure files end with newline
- **check-yaml** - Validate YAML syntax
- **check-added-large-files** - Prevent large file commits

---

## Architecture Decisions

See `docs/adr/` for key architectural decisions:

- [ADR 001](docs/adr/001-typer-cli-framework.md) - Why Typer for CLI
- [ADR 002](docs/adr/002-hexagonal-architecture.md) - Why Hexagonal Architecture
- [ADR 003](docs/adr/003-pytest-bdd-testing.md) - Why pytest-bdd for testing

## License

MIT License - see [LICENSE](LICENSE)
