#!/usr/bin/env python3
""" redis basics """
import redis
import uuid
from typing import Union, Callable, Optional


class Cache():
    """ cashe class """
    def __init__(self):
        """ initiates an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

"""    def store(self, data: Union[str, bytes, int, float]) -> str:
        "" store data using a random key ""
        uid = str(uuid.uuid4())
        self._redis.set(uid, data)
        return uid
    def get(self, key: str, fn: Callable = None) ->
            Union[str, bytes, int, float]:
        "" get the value from redis based on key
        and convert it to desired format ""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        "" get the value in string format
        from redis based on key""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> str:
        "" get the value in int format
        from redis based on key""
        return self.get(key, lambda x: int(x))
"""
    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves an integer value from a Redis data storage.
        '''
        return self.get(key, lambda x: int(x))
