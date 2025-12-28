"""Infrastructure layer - external adapters and implementations."""

from template_python_cli.infrastructure.config import (
    AppConfig,
    create_default_config,
    find_config_file,
    get_default_config_path,
    load_config,
)
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
    "AppConfig",
    "Verbosity",
    "colors_enabled",
    "create_default_config",
    "find_config_file",
    "get_console",
    "get_default_config_path",
    "get_error_console",
    "get_logger",
    "is_tty",
    "load_config",
    "setup_logging",
]
