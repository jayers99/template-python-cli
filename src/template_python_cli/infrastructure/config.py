"""Configuration file handling.

This module demonstrates configuration file patterns:
- Default config location (~/.config/myapp/config.toml)
- Override via --config flag
- Environment variable override (MYAPP_CONFIG)
- Config validation using Pydantic
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

# Try tomllib (Python 3.11+) or fall back to tomli
try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore[import-not-found,no-redef]


class AppConfig(BaseModel):
    """Application configuration model.

    Customize this model for your application's settings.
    Pydantic validates the config file contents.
    """

    # Example settings - customize for your app
    name: str = Field(default="default", description="Default name for greetings")
    verbose: bool = Field(default=False, description="Enable verbose output")
    quiet: bool = Field(default=False, description="Enable quiet mode")


def get_default_config_path() -> Path:
    """Get the default configuration file path.

    Returns:
        Path to the default config file (~/.config/template-cli/config.toml)
    """
    config_home = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    return Path(config_home) / "template-cli" / "config.toml"


def find_config_file(
    explicit_path: Path | None = None,
    env_var: str = "TEMPLATE_CLI_CONFIG",
) -> Path | None:
    """Find the configuration file to use.

    Priority (highest to lowest):
    1. Explicit path from --config flag
    2. Path from environment variable
    3. Default location (~/.config/template-cli/config.toml)

    Args:
        explicit_path: Path provided via --config flag.
        env_var: Environment variable name for config path.

    Returns:
        Path to config file, or None if no config file exists.
    """
    # 1. Explicit path takes priority
    if explicit_path is not None:
        if explicit_path.exists():
            return explicit_path
        return None  # Explicit path was given but doesn't exist

    # 2. Environment variable
    env_path = os.environ.get(env_var)
    if env_path:
        path = Path(env_path)
        if path.exists():
            return path

    # 3. Default location
    default_path = get_default_config_path()
    if default_path.exists():
        return default_path

    return None


def load_config(
    config_path: Path | None = None,
    env_var: str = "TEMPLATE_CLI_CONFIG",
) -> AppConfig:
    """Load configuration from file.

    Args:
        config_path: Explicit path from --config flag.
        env_var: Environment variable name for config path.

    Returns:
        AppConfig with loaded settings, or defaults if no config file.
    """
    path = find_config_file(config_path, env_var)

    if path is None:
        return AppConfig()

    return load_config_from_file(path)


def load_config_from_file(path: Path) -> AppConfig:
    """Load configuration from a specific file.

    Args:
        path: Path to the TOML config file.

    Returns:
        AppConfig with loaded settings.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file is invalid TOML or fails validation.
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        with open(path, "rb") as f:
            data: dict[str, Any] = tomllib.load(f)
    except Exception as e:
        raise ValueError(f"Invalid TOML in {path}: {e}") from e

    try:
        return AppConfig(**data)
    except Exception as e:
        raise ValueError(f"Config validation failed: {e}") from e


def create_default_config(path: Path | None = None) -> Path:
    """Create a default configuration file.

    Args:
        path: Where to create the config. Defaults to default location.

    Returns:
        Path to the created config file.
    """
    if path is None:
        path = get_default_config_path()

    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write default config
    default_content = """\
# Template CLI Configuration
# See documentation for all options

# Default name for the hello command
name = "World"

# Verbose output (true/false)
verbose = false

# Quiet mode - suppress non-error output (true/false)
quiet = false
"""
    path.write_text(default_content)
    return path
