"""Exit codes for CLI commands.

Following Unix conventions:
- 0: Success
- 1: General error
- 2: Misuse of shell command (invalid arguments)
- 64-78: Reserved for application-specific errors (BSD sysexits.h)
"""

from enum import IntEnum


class ExitCode(IntEnum):
    """Standard exit codes for the CLI.

    Usage:
        raise typer.Exit(ExitCode.SUCCESS)
        raise typer.Exit(ExitCode.VALIDATION_ERROR)
    """

    SUCCESS = 0
    GENERAL_ERROR = 1
    INVALID_ARGUMENT = 2
    VALIDATION_ERROR = 65  # EX_DATAERR - input data incorrect
    CONFIG_ERROR = 78  # EX_CONFIG - configuration error
