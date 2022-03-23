#!/usr/bin/env python3
""" Returns all students sorted by average score """
import pymongo


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    return mongo_collection.find().sort("averageScore")
