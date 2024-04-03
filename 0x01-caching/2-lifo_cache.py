#!/usr/bin/env python3
""" LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
