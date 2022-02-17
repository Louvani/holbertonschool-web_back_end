#!/usr/bin/env python3
"""
0x05. Personal data

    Examples of Personally Identifiable Information (PII)
    How to implement a log filter that will obfuscate PII fields
    How to encrypt a password and check the validity of an input password
    How to authenticate to a database using environment variables

"""

import logging
import os
import re
from typing import List

import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize RedactingFormatter
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    for field in fields:
        log = re.sub(f'(?<={field}=)[^{separator}]*', redaction, message)
    return log


def get_logger() -> logging.Logger:
    """Return a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
