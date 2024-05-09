import csv
from logger import Logger


class CSVLogger(Logger):
    """Concrete implementation of Logger for CSV logging."""

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def log_message(self, message):
        # Implementation specific to CSV logging
        pass
