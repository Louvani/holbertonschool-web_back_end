#!/usr/bin/python3
'''
Module
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' clss '''

    def __init__(self):
        ''' constructor  '''
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
        return self.cache_data.get(key)
