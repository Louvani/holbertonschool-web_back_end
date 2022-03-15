#!/usr/bin/env python3
'''Writing strings to Redis'''

from typing import Union, Optional, Callable
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Wraper to count calls of store'''
    key = method.__qualname__

    @wraps(method)
    def wrap(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrap


class Cache():

    parametrize = {}
    '''Keep cahe data into deisdb'''

    def __init__(self) -> None:
        '''Initialice a instace of redis'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[bytes, str, int, float]) -> str:
        '''Generate a raandom key for the data'''
        key = uuid.uuid4().__str__()
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        '''convert the data back to the desired format.'''
        value = self._redis.get(key)
        if value is None or fn is None:
            return value
        return fn(value)

    def get_str():
        pass

    def get_int():
        pass
