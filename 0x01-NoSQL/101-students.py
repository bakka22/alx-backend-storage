#!/usr/bin/env python3
""" avg score """
from pymongo import MongoClient


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    st_list = []
    pipeline = [{'$unwind': '$topics'}, {'$group': {'_id': '$_id',
                'name': {'$first': '$name'},
                'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': {'averageScore': -1}}]
    result = mongo_collection.aggregate(pipeline)
    for doc in result:
        st_list.append(doc)
    return st_list
