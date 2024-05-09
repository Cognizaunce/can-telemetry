from abc import ABC, abstractmethod

class Logger(ABC):
    """Abstract base class for logging operations."""

    @abstractmethod
    def log_message(self, message):
        """Log a message."""
        pass
