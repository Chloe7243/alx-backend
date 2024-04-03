#!/usr/bin/python3
""" Caching Implementation.
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used Caching Class"""

    def __init__(self):
        super().__init__()
        self.__stack = []

    def put(self, key, item):
        """Put an item in the cache"""
        if key and item:
            if self.cache_data.get(key):
                self.__stack.remove(key)
            self.cache_data.update({key: item})
            self.__stack.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                last_in = self.__stack.pop(-2)
                self.cache_data.pop(last_in)
                print(f"DISCARD: {last_in}")

    def get(self, key):
        """Get an item from the cache"""
        item = self.cache_data.get(key, None)
        if item:
            self.__stack.remove(key)
            self.__stack.append(key)
        return item
