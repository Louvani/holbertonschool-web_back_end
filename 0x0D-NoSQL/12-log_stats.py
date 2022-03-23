#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from multiprocessing import log_to_stderr
from pymongo import MongoClient


def main():
    """Displays stats of """
    client = MongoClient('mongodb://localhost:27017')
    nginx = client.logs.nginx

    data = {"numberOfLogs": count(nginx, {}),
            "get": count(nginx, {"method": "GET"}),
            "post": count(nginx, {"method": "POST"}),
            "put": count(nginx, {"method": "PUT"}),
            "patch": count(nginx, {"method": "PATCH"}),
            "delete": count(nginx, {"method": "DELETE"}),
            "status": count(nginx, {"path": "/status"}),
            }

    print(f"""{data["numberOfLogs"]} logs
Methods:
    method GET: {data["get"]}
    method POST: {data["post"]}
    method PUT: {data["put"]}
    method PATCH: {data["patch"]}
    method DELETE: {data["delete"]}
{data["status"]} status check""")


def count(collection, filter):
    return collection.count_documents(filter)


if __name__ == "__main__":
    main()
