#!/usr/bin/env python3
'''Writing strings to Redis'''

from ast import Call
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


def call_history(method: Callable) -> Callable:
    '''store the history of inputs and outputs for a particular function.'''
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrap(self, *args, **kwds):
        """wrap of decorator"""
        self._redis.rpush(inputs, str(args))
        returned_method = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(returned_method))
        return returned_method
    return wrap


def replay(method: Callable):
    '''display the history of calls of a particular function.'''
    get_self = method.__self__
    name = method.__qualname__
    key = get_self.get(name)

    if key:
        times = get_self.get_str(key)
        inputs = get_self._redis.lrange(name + ":inputs", 0, -1)
        outputs = get_self._redis.lrange(name + ":outputs", 0, -1)

        print(name + ' was called ' + times + 'times:')
        zipvalues = zip(inputs, outputs)
        result = list(zipvalues)
        for k, v in result:
            name_ = get_self.get_str(k)
            val = get_self.get_str(v)
            print(f"{name}(*{name_}) -> {val}")


class Cache():

    parametrize = {}
    '''Keep cahe data into deisdb'''

    def __init__(self) -> None:
        '''Initialice a instace of redis'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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

    def get_str(self, string: bytes) -> str:
        return string.decode("utf-8")


    def get_int(self, number: int) -> int:
        result = 0 * 256 + int(number)
        return result
