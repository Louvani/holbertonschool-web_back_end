#!/usr/bin/python3
"""
Module
"""


class BaseCaching():
    """ class """
    MAX_ITEMS = 4

    def __init__(self):
        """ construct"""
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ put an item in the cache"""
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key"""
        raise NotImplementedError(
            "get must be implemented in your cache class")
