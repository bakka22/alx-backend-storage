#!/usr/bin/env python3
""" insert to collection """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document into a collection """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
