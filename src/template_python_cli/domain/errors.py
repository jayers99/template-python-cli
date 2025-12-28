"""Domain-level errors.

These errors represent business logic failures that should be
translated to user-friendly messages at the CLI layer.
"""


class DomainError(Exception):
    """Base class for domain errors.

    All domain errors should inherit from this class.
    The CLI layer catches these and converts them to
    appropriate exit codes and user messages.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class ValidationError(DomainError):
    """Input validation failed.

    Raised when user input doesn't meet domain requirements.
    Maps to ExitCode.VALIDATION_ERROR.
    """

    pass
