"""Greeter service - example application layer component."""

from template_python_cli.domain.errors import ValidationError


def greet(name: str) -> str:
    """Generate a greeting for the given name.

    Args:
        name: The name to greet. Must be non-empty.

    Returns:
        A greeting string.

    Raises:
        ValidationError: If name is empty or whitespace-only.
    """
    if not name or not name.strip():
        raise ValidationError("Name cannot be empty")

    return f"Hello, {name.strip()}!"
