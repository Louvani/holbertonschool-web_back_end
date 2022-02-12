#!/usr/bin/python3
'''
Module
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' Function '''
    def put(self, key, item):
        ''' put a item to the dictionary '''
        if key and item:
            self.cache_data[key] = item
    def get(self, key):
        ''' Get the value associated with the given key '''
        return self.cache_data.get(key)
