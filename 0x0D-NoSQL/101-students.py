#!/usr/bin/env python3
""" Returns all students sorted by average score """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    return mongo_collection.aggregate([
        {"$project": {"averageScore": {"$avg": "$topics.score"}, "name": "$name"}},
        {"$sort": {"averageScore": -1}}
    ])
