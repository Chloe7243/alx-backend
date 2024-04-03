#!/usr/bin/env python3
""" LRU Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ Least Recently Used Caching Class
    """

    def __init__(self):
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            if self.cache_data.get(key):
                self.__queue.remove(key)
            self.cache_data.update({key: item})
            self.__queue.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                least_r_used = self.__queue.pop(0)
                self.cache_data.pop(least_r_used)
                print(f'DISCARD: {least_r_used}')

    def get(self, key):
        """ Get an item from the cache
        """
        item = self.cache_data.get(key, None)
        if item:
            self.__queue.remove(key)
            self.__queue.append(key)
        return item
