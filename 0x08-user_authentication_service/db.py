#!/usr/bin/env python3
"""Model DB with SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """
    DB class
    """
    session_args = ['id', 'email', 'hashed_password',
                    'session_id', 'reset_token']

    def __init__(self):
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Keep user in the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Return the first row in the users table after filtering
        """
        if not kwargs:
            raise InvalidRequestError
        for arg in kwargs:
            if arg not in self.session_args:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        use find_user_by to locate the user to update, then
        will update the user’s attributes as passed in the method’s
        arguments then commit changes to the database.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in self.session_args:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
