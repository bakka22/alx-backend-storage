#!/usr/bin/env python3
""" redis basics """
import redis
import uuid


class Cache():
    """ cashe class """
    def __init__(self):
        """ initiates an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """ store data using a random key """
        uid = str(uuid.uuid4())
        self._redis.set(uid, data)
        return uid
