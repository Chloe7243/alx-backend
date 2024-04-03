#!/usr/bin/env python3
""" Basic Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching
    """
    def put(self, key, item):
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        if key:
            return self.cache_data.get(key, None)
