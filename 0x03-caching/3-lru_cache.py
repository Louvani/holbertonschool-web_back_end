#!/usr/bin/python3
'''
Mudule 3. LRU Caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' clss LRUCache '''

    def __init__(self):
        ''' Construct LRUCache '''
        self.queue = []
        super().__init__()

    def put(self, key, item):
        ''' Aput the item to the dictionary '''
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        ''' get the value associated with the given key '''
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
