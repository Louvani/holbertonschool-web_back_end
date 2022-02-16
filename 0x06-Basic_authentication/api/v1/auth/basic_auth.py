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
        if not base64_authorization_header or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decode: str) -> (str, str):
        """Return the user email and password from the Base64 decoded
        """
        if (not isinstance(decode, str) or ':' not in decode):
            return (None, None)
        return (decode[:decode.find(':')], decode[decode.find(':') + 1:])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return the User instance based on email and password
        """
        if (user_email and user_pwd and isinstance(user_email, str) and
                isinstance(user_pwd, str)):
            try:
                users = User.search({'email': user_email})
            except Exception:
                return
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request
        """
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(b64)
        user, password = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(user, password)
