#!/usr/bin/env python3
""" LIFO Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item in the cache"""
        if key and item:
            cache_keys = list(self.cache_data.keys())
            l_index = len(cache_keys) - 1
            if len(cache_keys) == BaseCaching.MAX_ITEMS:
                self.cache_data.pop(cache_keys[l_index])
                print(f"DISCARD: {cache_keys[l_index]}")
            self.cache_data.update({key: item})

    def get(self, key):
        """Get an item from the cache"""
        if key:
            return self.cache_data.get(key, None)
