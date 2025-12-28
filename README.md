# template-python-cli

A Python CLI project template following Praxis governance patterns.

## What's Included

- **Hexagonal architecture** - `domain/`, `application/`, `infrastructure/` layers
- **Typer CLI framework** - Modern, type-hint-based CLI
- **BDD testing** - pytest-bdd with Gherkin feature files
- **Quality tools** - ruff (linting), mypy (type checking)
- **Pre-commit hooks** - Automated code quality checks
- **Poetry packaging** - Dependency management and packaging
- **PEP 561 compliant** - `py.typed` marker for type checker support

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

## CLI Patterns

This template demonstrates production CLI patterns:

### Exit Codes

```python
from template_python_cli.domain.exit_codes import ExitCode

raise typer.Exit(ExitCode.SUCCESS)           # 0
raise typer.Exit(ExitCode.GENERAL_ERROR)     # 1
raise typer.Exit(ExitCode.VALIDATION_ERROR)  # 65
```

### stdout/stderr Separation

```python
# Data output → stdout (safe for piping)
typer.echo(result)

# Diagnostics → stderr
typer.echo("Processing...", err=True)
```

### Flags

```bash
template-cli --version        # Show version
template-cli hello --verbose  # Detailed output
template-cli hello --quiet    # Errors only
```

### Environment Variables

Options can be configured via environment variables:

```bash
# Set via environment
export TEMPLATE_CLI_NAME="World"
template-cli hello              # Uses $TEMPLATE_CLI_NAME

# CLI flags override environment variables
template-cli hello Alice        # Ignores $TEMPLATE_CLI_NAME
```

```python
# In code: add envvar parameter to options
name: Annotated[str, typer.Argument(envvar="TEMPLATE_CLI_NAME")]
```

### Logging

Logging integrates with verbosity flags and outputs to stderr:

```python
from template_python_cli.infrastructure import setup_logging, Verbosity

setup_logging(Verbosity.VERBOSE)  # DEBUG level
setup_logging(Verbosity.NORMAL)   # INFO level (default)
setup_logging(Verbosity.QUIET)    # WARNING level
```

### TTY Detection and Colors

Colors are automatically disabled when piped or when `NO_COLOR` is set:

```python
from template_python_cli.infrastructure import get_console, is_tty

console = get_console()
console.print("[bold green]Success![/bold green]")  # Rich markup

if is_tty():
    # Interactive terminal - show progress
    pass
```

```bash
# Colors disabled automatically when piped
template-cli info | cat

# Or explicitly via environment
NO_COLOR=1 template-cli info
```

### Multiple Commands

The template includes multiple commands demonstrating subcommand patterns:

```bash
template-cli hello World    # Greet command
template-cli info           # Show environment info
```

### Error Handling

Domain errors are caught at the CLI layer and converted to user-friendly messages with appropriate exit codes:

```python
except ValidationError as e:
    err_console.print(f"[red]Error:[/red] {e.message}")
    raise typer.Exit(ExitCode.VALIDATION_ERROR) from None
```

### Configuration Files

The CLI supports TOML configuration files with priority resolution:

1. `--config` flag (explicit path)
2. `TEMPLATE_CLI_CONFIG` environment variable
3. `~/.config/template-cli/config.toml` (default location)

**Create a config file:**

```bash
# Create default config at ~/.config/template-cli/config.toml
template-cli config --init

# Create at custom location
template-cli config --init --path ./config.toml
```

**View config status:**

```bash
template-cli config      # Show config file location and current settings
template-cli info        # Show config in environment info
```

**Example config.toml:**

```toml
# Template CLI Configuration
name = "World"      # Default name for hello command
verbose = false     # Enable verbose output
quiet = false       # Enable quiet mode
```

**Using config in code:**

```python
from template_python_cli.infrastructure import load_config, AppConfig

# Load with automatic resolution
config = load_config()

# Load from specific path
config = load_config(Path("./my-config.toml"))

# Access settings
print(config.name)      # Default name
print(config.verbose)   # Verbose setting
```

---

## Shell Completion

Typer provides built-in shell completion support.

**Install completion:**

```bash
# For bash
template-cli --install-completion bash

# For zsh
template-cli --install-completion zsh

# For fish
template-cli --install-completion fish
```

**Show completion script (without installing):**

```bash
template-cli --show-completion bash
```

After installation, restart your shell or source the config file.

---

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
