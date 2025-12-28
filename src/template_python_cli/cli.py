"""CLI entry point using Typer.

This module demonstrates key CLI patterns:
- Exit codes (ExitCode enum)
- stdout/stderr separation (data vs diagnostics)
- --version flag
- --verbose/--quiet flags
- Error handling (domain errors → user messages)
"""

from typing import Annotated

import typer

from template_python_cli import __version__
from template_python_cli.application.greeter import greet
from template_python_cli.domain.errors import DomainError, ValidationError
from template_python_cli.domain.exit_codes import ExitCode

app = typer.Typer(
    name="template-cli",
    help="A Python CLI template following Praxis patterns.",
    no_args_is_help=True,
)


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        # Version is data → stdout
        typer.echo(f"template-cli {__version__}")
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
    name: Annotated[str, typer.Argument(help="Name to greet.")],
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed output."),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option("--quiet", "-q", help="Show only errors."),
    ] = False,
) -> None:
    """Greet someone by name.

    Examples:
        template-cli hello World
        template-cli hello --verbose Alice
        template-cli hello --quiet Bob
    """
    try:
        # Verbose diagnostics → stderr
        if verbose and not quiet:
            typer.echo(f"Processing greeting for: {name}", err=True)

        result = greet(name)

        # Data output → stdout (for piping)
        if not quiet:
            typer.echo(result)

        if verbose and not quiet:
            typer.echo("Greeting completed successfully.", err=True)

        raise typer.Exit(ExitCode.SUCCESS)

    except ValidationError as e:
        # Error messages → stderr
        typer.echo(f"Error: {e.message}", err=True)
        typer.echo("Hint: Provide a non-empty name.", err=True)
        raise typer.Exit(ExitCode.VALIDATION_ERROR) from None

    except DomainError as e:
        typer.echo(f"Error: {e.message}", err=True)
        raise typer.Exit(ExitCode.GENERAL_ERROR) from None


if __name__ == "__main__":
    app()
