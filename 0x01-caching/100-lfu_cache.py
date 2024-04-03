#!/usr/bin/env python3
""" LFU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
        self.lfu_keys = []
        self.lfu_count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu_count[key] += 1
                self.lfu_keys.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_lfu = min(self.lfu_count.values())
                    min_keys = [k for k in self.lfu_count if self.lfu_count[k] == min_lfu]
                    discard = min_keys[0]
                    for k in min_keys:
                        if len(self.cache_data[k]) < len(self.cache_data[discard]):
                            discard = k
                    print('DISCARD:', discard)
                    del self.cache_data[discard]
                    del self.lfu_count[discard]
                    self.lfu_keys.remove(discard)
                self.cache_data[key] = item
                self.lfu_count[key] = 1
            self.lfu_keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.lfu_count[key] += 1
            self.lfu_keys.remove(key)
            self.lfu_keys.append(key)
            return self.cache_data[key]
        return None
