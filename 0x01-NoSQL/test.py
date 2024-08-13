#!/usr/bin/env python3
""" get all from collection """
from pymongo import MongoClient


client = MongoClient()
db = client.test
col = db.test
print(col.count_documents({}))
