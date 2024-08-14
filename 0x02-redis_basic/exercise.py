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
     def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Gets key's value from redis and converts
            result byte  into correct data type
        """
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers
        """
        return int(data)
