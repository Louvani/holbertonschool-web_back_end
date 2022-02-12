#!/usr/bin/python3
'''
Module
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' Class MRUCache '''

    def __init__(self):
        ''' Construct MRUCache '''
        self.stack = []
        super().__init__()

    def put(self, key, item):
        ''' put the item to the dictionary '''
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' get the value associated with the given key '''
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
