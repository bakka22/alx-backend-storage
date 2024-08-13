#!/usr/bin/env python3
""" match by topics """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    tmp = []
    for doc in mongo_collection.find({"topics": topic}):
        tmp.append(doc)
    return tmp
