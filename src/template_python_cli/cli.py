"""CLI entry point."""

from typing import Annotated

import typer

from template_python_cli import __version__
from template_python_cli.domain.greeter import greet

app = typer.Typer(add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"template-python-cli {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option("--version", "-V", help="Show version and exit.", callback=version_callback, is_eager=True),
    ] = False,
) -> None:
    """A Python CLI template following Praxis patterns."""


@app.command()
def hello(name: Annotated[str, typer.Argument(help="Name to greet.")]) -> None:
    """Greet someone by name."""
    try:
        typer.echo(greet(name))
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None
