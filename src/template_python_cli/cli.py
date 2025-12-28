"""CLI entry point using Typer.

This module demonstrates key CLI patterns:
- Exit codes (ExitCode enum)
- stdout/stderr separation (data vs diagnostics)
- --version flag
- --verbose/--quiet flags
- Error handling (domain errors -> user messages)
- Environment variable configuration
- Logging integration
- TTY detection and color handling
- Multiple commands pattern
"""

from typing import Annotated

import typer

from template_python_cli import __version__
from template_python_cli.application.greeter import greet
from template_python_cli.domain.errors import DomainError, ValidationError
from template_python_cli.domain.exit_codes import ExitCode
from template_python_cli.infrastructure import (
    Verbosity,
    get_console,
    get_error_console,
    get_logger,
    is_tty,
    setup_logging,
)

app = typer.Typer(
    name="template-cli",
    help="A Python CLI template following Praxis patterns.",
    no_args_is_help=True,
)


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console = get_console()
        console.print(f"template-cli {__version__}")
        raise typer.Exit(ExitCode.SUCCESS)


@app.callback()
def main(
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            "-V",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit.",
        ),
    ] = None,
) -> None:
    """Template Python CLI - demonstrating Praxis patterns."""
    pass


@app.command()
def hello(
    name: Annotated[
        str,
        typer.Argument(
            help="Name to greet.",
            envvar="TEMPLATE_CLI_NAME",  # Environment variable support
        ),
    ],
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            "-v",
            help="Show detailed output.",
            envvar="TEMPLATE_CLI_VERBOSE",
        ),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option(
            "--quiet",
            "-q",
            help="Show only errors.",
            envvar="TEMPLATE_CLI_QUIET",
        ),
    ] = False,
) -> None:
    """Greet someone by name.

    Examples:
        template-cli hello World
        template-cli hello --verbose Alice
        TEMPLATE_CLI_NAME=Bob template-cli hello
    """
    # Set up logging based on verbosity
    if quiet:
        verbosity = Verbosity.QUIET
    elif verbose:
        verbosity = Verbosity.VERBOSE
    else:
        verbosity = Verbosity.NORMAL
    setup_logging(verbosity)
    logger = get_logger()

    console = get_console()
    err_console = get_error_console()

    try:
        logger.debug(f"Processing greeting for: {name}")

        result = greet(name)

        # Data output -> stdout (for piping)
        if not quiet:
            console.print(result)

        logger.debug("Greeting completed successfully.")
        raise typer.Exit(ExitCode.SUCCESS)

    except ValidationError as e:
        err_console.print(f"[red]Error:[/red] {e.message}")
        err_console.print("[dim]Hint: Provide a non-empty name.[/dim]")
        raise typer.Exit(ExitCode.VALIDATION_ERROR) from None

    except DomainError as e:
        err_console.print(f"[red]Error:[/red] {e.message}")
        raise typer.Exit(ExitCode.GENERAL_ERROR) from None


@app.command()
def info() -> None:
    """Show environment and configuration information.

    Demonstrates multiple commands pattern and environment detection.

    Examples:
        template-cli info
    """
    console = get_console()

    # Show version
    console.print(f"[bold]template-cli[/bold] v{__version__}")
    console.print()

    # Show environment detection
    console.print("[bold]Environment:[/bold]")
    console.print(f"  TTY detected: {is_tty()}")

    import os

    no_color = os.environ.get("NO_COLOR")
    console.print(f"  NO_COLOR: {'set' if no_color is not None else 'not set'}")

    # Show relevant environment variables
    console.print()
    console.print("[bold]Environment Variables:[/bold]")
    env_vars = [
        ("TEMPLATE_CLI_NAME", "Default name for hello command"),
        ("TEMPLATE_CLI_VERBOSE", "Enable verbose output"),
        ("TEMPLATE_CLI_QUIET", "Enable quiet mode"),
    ]
    for var, desc in env_vars:
        value = os.environ.get(var)
        if value:
            console.print(f"  {var}={value}")
        else:
            console.print(f"  {var} [dim](not set - {desc})[/dim]")

    raise typer.Exit(ExitCode.SUCCESS)


if __name__ == "__main__":
    app()
