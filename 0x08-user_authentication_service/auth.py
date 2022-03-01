#!/usr/bin/env python3
""" Auth Module """
import uuid

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    takes in a password string arguments and returns bytes.
    """
    hash_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hash_password


def _generate_uuid() -> str:
    """
    Generate a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        take mandatory email and
        password string arguments and return a User object.
        """
        try:
            self._db.find_user_by(email=email):
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate password credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create session and returning it's ID
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id
        except Exception:
            return

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Get the user corresponding to the session ID or None
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return

    def destroy_session(self, user_id: int) -> None:
        """
        destroy a user's session
        """
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Rest a new password based on it's email
        """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update user password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            new_password = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=new_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
