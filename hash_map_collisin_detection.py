""" This is an extension of the hash map without collision detection.
This implements collision detection  and handles it using seperate chaining"""

import pprint

class HashMap:
    def __init__(self):
        self.MAX = 20  # for the underlying array size
        self.arr = [[] for _ in range(self.MAX)]

    # this function calculates the hash of the given key
    def get_hash(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        # Iterate over every (key, value) pair tuple in the array
        for indx, element in enumerate(self.arr[h]):
            # get the key on the (key, value) pair
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for indx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key: # Element represents (key, value) pair tuple
                self.arr[h][indx] = (key, value) # At a certain index in the list of list, update it with (key, value)
                found = True
                break
        if not found:
                self.arr[h].append((key, value))


    def __delitem__(self, key):
        h = self.get_hash(key)
        for indx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][indx]


# Test drive

hasht = HashMap()

hasht['march 6'] = 23
hasht['march 17'] = 27
hasht['march 3'] = 37
hasht['march 1'] = 65
hasht['march 23'] = 26
hasht['march 26'] = 54
hasht['march 30'] = 27

pprint.pprint(hasht.arr)

print('--------------------------------------------------------------------')

del hasht["march 26"]

pprint.pprint(hasht.arr)

