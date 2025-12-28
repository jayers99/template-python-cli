"""Shared test fixtures."""

import pytest
from typer.testing import CliRunner

from template_python_cli.cli import app


@pytest.fixture
def cli_runner() -> CliRunner:
    """Provide a Typer CLI test runner."""
    return CliRunner()


@pytest.fixture
def run_cli(cli_runner: CliRunner):
    """Provide a helper function to run CLI commands."""

    def _run(*args: str, catch_exceptions: bool = False):
        return cli_runner.invoke(app, list(args), catch_exceptions=catch_exceptions)

    return _run
