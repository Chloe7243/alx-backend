#!/usr/bin/python3
""" Caching Implementation.
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used Caching Class"""

    def __init__(self):
        super().__init__()
        self.__queue = []
        self.__trackpad = {}

    def put(self, key, item):
        """Put an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.__trackpad[key] += 1
                self.__queue.remove(key)
            else:
                self.__trackpad[key] = 1

            self.cache_data[key] = item
            self.__queue.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                # print(self.__trackpad)
                # print(self.__queue)
                # print(self.cache_data)
                trackpad = self.__trackpad.copy()
                trackpad.pop(key)
                least_f_used = min(
                    trackpad, key=lambda k: (trackpad[k], self.__queue.index(k)
                                             )
                )
                # min_freq = min(trackpad.values())
                # mf_keys = [k for k, f in trackpad.items() if f == min_freq]
                # least_f_used = min(mf_keys,
                #                    key=lambda k: self.__queue.index(k))

                self.__trackpad.pop(least_f_used)
                self.__queue.remove(least_f_used)
                self.cache_data.pop(least_f_used)
                print(f"DISCARD: {least_f_used}")

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            self.__trackpad[key] += 1
            self.__queue.remove(key)
            self.__queue.append(key)

        return self.cache_data.get(key, None)
