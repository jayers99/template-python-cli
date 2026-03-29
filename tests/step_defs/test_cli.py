"""Step definitions for CLI feature tests."""

import pytest
from pytest_bdd import parsers, scenarios, then, when
from typer.testing import CliRunner

from template_python_cli.cli import app

scenarios("../features/cli.feature")


@pytest.fixture()
def cli_runner() -> CliRunner:
    return CliRunner()


@pytest.fixture()
def result() -> dict:
    return {}


@when(parsers.parse('I run the CLI with "{args}"'))
def run_cli_with_args(cli_runner: CliRunner, result: dict, args: str) -> None:
    result["output"] = cli_runner.invoke(app, args.split())


@when("I greet with whitespace")
def run_cli_greet_whitespace(cli_runner: CliRunner, result: dict) -> None:
    result["output"] = cli_runner.invoke(app, ["hello", "   "])


@then(parsers.parse("the exit code is {code:d}"))
def check_exit_code(result: dict, code: int) -> None:
    assert result["output"].exit_code == code, (
        f"Expected exit code {code}, got {result['output'].exit_code}. "
        f"Output: {result['output'].output}"
    )


@then(parsers.parse('the output contains "{text}"'))
def check_output_contains(result: dict, text: str) -> None:
    output = result["output"].output
    assert text in output, f"Expected '{text}' in output. Got: {output}"


@then(parsers.parse('the error output contains "{text}"'))
def check_error_contains(result: dict, text: str) -> None:
    # CliRunner without mix_stderr=False puts everything in output
    output = result["output"].output
    assert text in output, f"Expected '{text}' in output. Got: {output}"
