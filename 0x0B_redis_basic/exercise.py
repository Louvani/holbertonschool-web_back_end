#!/usr/bin/env python3
'''Writing strings to Redis'''

import redis
import uuid

class Cache():
    def __init__(self) -> None:
        self._redis = redis.Redis()

    def store(self, data) -> str:
        key = uuid.uuid4().__str__()
        self._redis.set(key, data)
        return key
