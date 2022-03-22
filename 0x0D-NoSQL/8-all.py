#!/usr/bin/env python3
"""Module to list all documents in mongodb"""


def list_all(mongo_collection):
    """function that lists all documents in a collection:"""
    if mongo_collection.count_documents == 0:
        return []
    else:
        return mongo_collection.find()
