#!/usr/bin/env python3
"""
BasicAuth
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class to manage API authentication
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header for a
        Basic Authentication
        """
        if not authorization_header:
            return None
        if (isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return authorization_header[6:]
        return None

def decode_base64_authorization_header(
        self, base64_authorization_header: str) -> str:
    """Returns the decoded value of a Base64 string
    base64_authorization_header"""
    if not base64_authorization_header or not isinstance(base64_authorization_header, str):
        return None
    try:
        return base64.b64decode(
            base64_authorization_header.encode('utf-8')).decode('utf-8')
    except Exception:
        return None
