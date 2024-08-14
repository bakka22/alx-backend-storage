#!/usr/bin/env python3
""" redis basics """
import redis
import uuid
from typing import Union


class Cache():
    """ cashe class """
    def __init__(self):
        """ initiates an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data using a random key """
        uid = str(uuid.uuid4())
        self._redis.set(uid, data)
        return uid

    def get(self, key, fn):
        """ get the value from redis based on key
        and convert it to desired format """
        value = self._redis.get(key)
        if fn and value:
            value = fn(value)
        return value

    def get_str(self, key):
        """ get the value in string format
        from redis based on key"""
        self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """ get the value in int format
        from redis based on key"""
        self.get(key, int)
