#!/usr/bin/env python3
""" get all from collection """


def list_all(mongo_collection):
    """ lists all documents in a collection """
    tmp = []
    for doc in mongo_collection.find():
        tmp.append(doc)
    return tmp
