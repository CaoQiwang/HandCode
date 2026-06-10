import sys
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.data = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]
        else:
            return -1
    
    def put(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            if len(self.data) >= self.capacity:
                self.data.popitem()
            self.data[key] = value
        self.data.move_to_end(key)


if __name__ == "__main__":
    capacity = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    lru_cache = LRUCache(capacity)
    for _ in range(n):
        parts = sys.stdin.readline().strip().split()
        if parts[0] == 'get':
            key = parts[1]
            lru_cache.get(key)
        if parts[0] == 'put':
            key = parts[1]
            value = int(parts[2])
            lru_cache.put(key, value)
        
