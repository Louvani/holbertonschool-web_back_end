#!/usr/bin/env python3
"""Authorization module to manage API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Chack path in the list of exluded paths"""
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return None"""
        if request is None:
            return None
        return request.header.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None
