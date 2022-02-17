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


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    for field in fields:
        log = re.sub(f'(?<={field}=)[^{separator}]*', redaction, message)
    return log
