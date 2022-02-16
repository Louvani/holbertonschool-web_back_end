#!/usr/bin/env python3
"""
BasicAuth
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class to manage API authentication
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header for a Basic Authentication
        """
        if not authorization_header:
            return None
        if (isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return authorization_header[6:]
        return None
