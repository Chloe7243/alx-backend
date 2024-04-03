#!/usr/bin/env python3
""" FIFO Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            cache_keys = list(self.cache_data.keys())
            if len(cache_keys) == BaseCaching.MAX_ITEMS:
                self.cache_data.pop(cache_keys[0])
                print(f"DISCARD: {cache_keys[0]}")
            self.cache_data.update({key: item})

    def get(self, key):
        if key:
            return self.cache_data.get(key, None)
