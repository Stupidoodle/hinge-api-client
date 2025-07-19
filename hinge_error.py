"""Exceptions for the Hinge API Client."""


class HingeError(Exception):
    """Base exception for all Hinge client related errors."""


class HingeAuthError(HingeError):
    """Exception raised for authentication errors."""

    def __init__(
        self, message="Authentication failed. Please check your credentials."
    ):
        """Initialize the HingeAuthError with a custom message.

        Args:
            message (str): Error message to display.

        """
        super().__init__(message)
