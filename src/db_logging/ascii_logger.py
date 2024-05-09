from logger import Logger


class ASCIILogger(Logger):
    """Concrete implementation of Logger for ASCII file logging."""

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def log_message(self, message):
        # Implementation specific to ASCII file logging
        pass
