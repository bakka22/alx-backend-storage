#!/usr/bin/env python3
""" nginx logs """
from pymongo import MongoClient

if __name__ == "__main__":
    reqs = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    req_dic = {'GET': 0, 'POST': 0, 'PUT': 0, 'PATCH': 0, 'DELETE': 0}
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    print(f"{collection.count_documents({})} logs")
    pipeline = [
        {'$match': {'method': {'$in': reqs}}},
        {'$group': {'_id': '$method', 'sum': {'$sum': 1}}}
    ]
    print("Methods:")
    result = collection.aggregate(pipeline)
    for doc in result:
        if doc['_id'] in reqs:
            req_dic[doc['_id']] = doc['sum']
    for req in reqs:
        print(f"\tmethod {req}: {req_dic[req]}")
    st_checks = collection.count_documents({"method": 'GET', "path": "/status"})
    print(f"{st_checks} status check")
