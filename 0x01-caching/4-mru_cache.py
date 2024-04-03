#!/usr/bin/python3
""" Fifo Cache Doc """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ class documenation """
    def __init__(self):
        """ init documentation"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put documentation"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(-1)
                self.cache_data.pop(removed)
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """get documentation """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
        else:
            return None
