#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
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

    print(f'{data["numberOfLogs"]} logs')
    print('Methods:')
    print('\tmethod GET:', data["get"])
    print('\tmethod POST:', data["post"])
    print('\tmethod PUT:', data["put"])
    print('\tmethod PATCH:', data["patch"])
    print('\tmethod DELETE:', data["delete"])
    print(data["status"], 'status check')


def count(collection, filter):
    """Count the number of documments"""
    return collection.count_documents(filter)


if __name__ == "__main__":
    main()
