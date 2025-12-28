"""Console output handling with TTY detection and color support.

This module provides:
- TTY detection (is output going to a terminal or a pipe?)
- NO_COLOR environment variable support
- Rich console for colored output when appropriate
"""

import os
import sys

from rich.console import Console


def is_tty() -> bool:
    """Check if stdout is connected to a TTY.

    Returns:
        True if stdout is a terminal, False if piped/redirected.
    """
    return sys.stdout.isatty()


def colors_enabled() -> bool:
    """Check if colors should be enabled.

    Colors are disabled when:
    - NO_COLOR environment variable is set (any value)
    - TERM is "dumb"
    - Output is not a TTY (piped/redirected)

    Returns:
        True if colors should be used, False otherwise.
    """
    if os.environ.get("NO_COLOR") is not None:
        return False
    if os.environ.get("TERM") == "dumb":
        return False
    return is_tty()


def get_console(force_terminal: bool | None = None) -> Console:
    """Get a Rich console configured for the current environment.

    Args:
        force_terminal: Override TTY detection. None = auto-detect.

    Returns:
        Configured Rich Console instance.
    """
    if force_terminal is None:
        force_terminal = is_tty()

    return Console(
        force_terminal=force_terminal,
        no_color=not colors_enabled(),
        stderr=False,  # Use stdout for data
    )


def get_error_console() -> Console:
    """Get a Rich console for error/diagnostic output (stderr).

    Returns:
        Configured Rich Console instance for stderr.
    """
    return Console(
        force_terminal=sys.stderr.isatty(),
        no_color=not colors_enabled(),
        stderr=True,
    )
