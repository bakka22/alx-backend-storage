#!/usr/bin/python3


Cache = __import__('exercise').Cache
cache = Cache()
print(cache.store(b"first"))
print(cache.get(cache.store.__qualname__))
print(cache.store(b"second"))
print(cache.store(b"third"))
print(cache.get(cache.store.__qualname__))
