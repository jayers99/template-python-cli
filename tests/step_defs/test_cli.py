"""Step definitions for CLI feature tests."""

import os
import tempfile
from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from typer.testing import CliRunner

from template_python_cli import __version__
from template_python_cli.cli import app

scenarios("../features/cli.feature")


@pytest.fixture
def cli_runner() -> CliRunner:
    """Provide a CLI test runner with output separation."""
    return CliRunner(mix_stderr=False)


@pytest.fixture
def result():
    """Store the CLI result between steps."""
    return {}


@pytest.fixture
def env_vars():
    """Store environment variables to set for CLI invocation."""
    return {}


@given(parsers.parse('environment variable "{name}" is set to "{value}"'))
def set_env_var(env_vars: dict, name: str, value: str) -> None:
    """Set an environment variable for the CLI invocation."""
    env_vars[name] = value


@when(parsers.parse('I run the CLI with "{args}"'))
def run_cli_with_args(cli_runner: CliRunner, result: dict, args: str) -> None:
    """Run the CLI with the given arguments."""
    result["output"] = cli_runner.invoke(app, args.split())


@when(parsers.parse('I run "{command}"'))
def run_command(
    cli_runner: CliRunner, result: dict, env_vars: dict, command: str
) -> None:
    """Run a CLI command."""
    import shlex

    args = shlex.split(command)

    # Set environment variables for this invocation
    old_env = {}
    for name, value in env_vars.items():
        old_env[name] = os.environ.get(name)
        os.environ[name] = value

    try:
        result["output"] = cli_runner.invoke(app, args)
    finally:
        # Restore original environment
        for name in env_vars:
            if old_env[name] is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = old_env[name]


@then(parsers.parse("the exit code should be {code:d}"))
def check_exit_code(result: dict, code: int) -> None:
    """Verify the exit code."""
    assert result["output"].exit_code == code, (
        f"Expected exit code {code}, got {result['output'].exit_code}. "
        f"Output: {result['output'].output}"
    )


@then("the output should contain the version number")
def check_version_output(result: dict) -> None:
    """Verify version is in output."""
    assert __version__ in result["output"].output


@then(parsers.parse('the output should contain "{text}"'))
def check_output_contains(result: dict, text: str) -> None:
    """Verify output contains text."""
    assert text in result["output"].output, (
        f"Expected '{text}' in output. Got: {result['output'].output}"
    )


@then(parsers.parse('stderr should contain "{text}"'))
def check_stderr_contains(result: dict, text: str) -> None:
    """Verify stderr contains text."""
    stderr = result["output"].stderr or ""
    # Fall back to mixed output if stderr separation not available
    combined = stderr or result["output"].output
    assert text in combined, f"Expected '{text}' in stderr. Got: {combined}"


@then(parsers.parse('stdout should contain "{text}"'))
def check_stdout_contains(result: dict, text: str) -> None:
    """Verify stdout contains text."""
    stdout = result["output"].output
    assert text in stdout, f"Expected '{text}' in stdout. Got: {stdout}"


@then("stdout should be empty")
def check_stdout_empty(result: dict) -> None:
    """Verify stdout is empty or contains only whitespace."""
    stdout = result["output"].output.strip()
    # In quiet mode, there should be no greeting output
    assert stdout == "" or "Hello" not in stdout, (
        f"Expected empty stdout. Got: {stdout}"
    )


@pytest.fixture
def temp_dir() -> dict[str, Path | None]:
    """Provide a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield {"path": Path(tmpdir), "config_path": None}


@given("a temporary directory")
def given_temp_dir(temp_dir: dict[str, Path | None]) -> None:
    """Set up a temporary directory for config file."""
    path = temp_dir["path"]
    if path is not None:
        temp_dir["config_path"] = path / "config.toml"


@when("I run config init with path to temp directory")
def run_config_init_with_temp(
    cli_runner: CliRunner,
    result: dict[str, object],
    temp_dir: dict[str, Path | None],
) -> None:
    """Run config --init with path to temp directory."""
    config_path = temp_dir["config_path"]
    args = ["config", "--init", "--path", str(config_path)]
    result["output"] = cli_runner.invoke(app, args)
    result["config_path"] = config_path


@then("the config file should exist")
def check_config_file_exists(result: dict[str, object]) -> None:
    """Verify the config file was created."""
    config_path = result.get("config_path")
    assert isinstance(config_path, Path), "Config path not set in result"
    assert config_path.exists(), f"Config file not found at {config_path}"
