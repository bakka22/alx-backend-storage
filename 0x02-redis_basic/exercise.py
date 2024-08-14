#!/usr/bin/env python3
""" redis basics """
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ Decorator for Cache class methods to track call history"""
    @wraps(method)
    def wrapper(self: Any, *args):
        """ wraps called method """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        out = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", out)
        return out
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache class methods to track call count """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs):
        """ wraps called method """
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwargs)
    return wrapper


def replay(fn: Callable):
    """ print the call history of a function """
    r = redis.Redis()
    name = fn.__qualname__

    def de(x):
        return x.decode('utf-8')
    inputs = r.lrange(f"{name}:inputs", 0, -1)
    outputs = r.lrange(f"{name}:outputs", 0, -1)
    zipped = list(zip(inputs, outputs))
    print(f"{name} was called {len(zipped)} times:")
    for tup in zipped:
        print(f"{name}(*{de(tup[0])}) -> {de(tup[1])}")


class Cache():
    """ cashe class """
    def __init__(self):
        """ initiates an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data using a random key """
        uid = str(uuid.uuid4())
        self._redis.set(uid, data)
        return uid

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """ get the value from redis based on key
        and convert it to desired format """
        value = self._redis.get(key)
        if fn and value:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ get the value in string format
        from redis based on key"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> str:
        """ get the value in int format
        from redis based on key"""
        return self.get(key, lambda x: int(x))
