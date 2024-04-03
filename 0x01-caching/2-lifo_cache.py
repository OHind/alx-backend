#!/usr/bin/python3
""" Fifo Cache Doc """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ class documenation """
    def __init__(self):
        """ init documentation"""
        super().__init__()

    def put(self, key, item):
        """ put documentation"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item

    def get(self, key):
        """get documentation """
        if key:
            return self.cache_data.get(key)
        else:
            return None
