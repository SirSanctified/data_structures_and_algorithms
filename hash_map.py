"""This is a simple illustration of the python implementation of the hash map data
structure. it will not contain any collision detection or handling mechanisms"""


class HashMap:
    def __init__(self):
        self.MAX = 20  # for the underlying array size
        self.arr = [None for _ in range(self.MAX)]

    # this function calculates the hash of the given key
    def get_hash(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


# Test drive

hash_map = HashMap()
hash_map["pritchard"] = 24
hash_map["promise"] = 20
hash_map["pamela"] = 16

print(hash_map["pritchard"], hash_map["promise"], hash_map["pamela"])

del hash_map["promise"]

print(hash_map.arr)
