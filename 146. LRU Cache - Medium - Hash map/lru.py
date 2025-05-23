from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with given capacity.
        :param capacity: Maximum number of items cache can hold
        """
        self.capacity = capacity
        self.cache = OrderedDict()  # Stores key-value pairs maintaining insertion order

    def get(self, key: int) -> int:
        """
        Retrieve the value of the key if present in the cache.
        Moves the key to the end to mark it as recently used.
        Returns -1 if the key is not present.
        :param key: Key to retrieve from cache
        :return: Value associated with the key or -1 if not found
        """
        if key not in self.cache:
            return -1  # Key not found

        # Move the accessed key to the end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of the key.
        Moves the key to the end to mark it as recently used.
        If capacity is exceeded, evicts the least recently used item.
        :param key: Key to insert or update
        :param value: Value associated with the key
        """
        if key in self.cache:
            # Move existing key to the end before updating
            self.cache.move_to_end(key)
        self.cache[key] = value  # Insert or update key-value pair

        if len(self.cache) > self.capacity:
            # Remove the least recently used item (first inserted)
            self.cache.popitem(last=False)
