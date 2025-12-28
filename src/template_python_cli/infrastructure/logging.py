"""Logging configuration for CLI applications.

Logging is configured based on verbosity level:
- quiet: WARNING and above only
- normal: INFO and above
- verbose: DEBUG and above

All logs go to stderr to keep stdout clean for data output.
"""

import logging
import sys
from enum import IntEnum


class Verbosity(IntEnum):
    """Verbosity levels for CLI output."""

    QUIET = 0
    NORMAL = 1
    VERBOSE = 2


def setup_logging(verbosity: Verbosity = Verbosity.NORMAL) -> logging.Logger:
    """Configure logging based on verbosity level.

    Args:
        verbosity: The desired verbosity level.

    Returns:
        Configured logger instance.
    """
    level_map = {
        Verbosity.QUIET: logging.WARNING,
        Verbosity.NORMAL: logging.INFO,
        Verbosity.VERBOSE: logging.DEBUG,
    }

    level = level_map.get(verbosity, logging.INFO)

    # Configure root logger
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,  # Logs go to stderr, not stdout
        force=True,
    )

    logger = logging.getLogger("template_python_cli")
    logger.setLevel(level)

    return logger


def get_logger() -> logging.Logger:
    """Get the application logger.

    Returns:
        The application logger instance.
    """
    return logging.getLogger("template_python_cli")
