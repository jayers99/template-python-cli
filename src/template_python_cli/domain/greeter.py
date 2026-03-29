"""Greeting logic."""


def greet(name: str) -> str:
    """Return a greeting for the given name.

    Raises:
        ValueError: If name is empty or whitespace.
    """
    stripped = name.strip()
    if not stripped:
        raise ValueError("Name cannot be empty")
    return f"Hello, {stripped}!"
