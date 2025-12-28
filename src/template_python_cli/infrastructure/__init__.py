"""Infrastructure layer - external adapters and implementations."""

from template_python_cli.infrastructure.console import (
    colors_enabled,
    get_console,
    get_error_console,
    is_tty,
)
from template_python_cli.infrastructure.logging import (
    Verbosity,
    get_logger,
    setup_logging,
)

__all__ = [
    "Verbosity",
    "colors_enabled",
    "get_console",
    "get_error_console",
    "get_logger",
    "is_tty",
    "setup_logging",
]
