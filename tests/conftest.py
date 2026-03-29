"""Shared test fixtures."""

import pytest
from typer.testing import CliRunner

from template_python_cli.cli import app


@pytest.fixture()
def cli_runner() -> CliRunner:
    return CliRunner()


@pytest.fixture()
def run_cli(cli_runner: CliRunner):
    def _run(*args: str):
        return cli_runner.invoke(app, list(args))

    return _run
