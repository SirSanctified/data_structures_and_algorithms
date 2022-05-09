""" This hash map implementation uses linear probing to handle collisions"""

import pprint

class HashMap:
    def __init__(self):
        self.MAX = 10  # for the underlying array size
        self.arr = [[None, None] for _ in range(self.MAX)]
        # Store (key, value) pairs in an underlying list
        # This will make it easier to get the value by its key even if it gets placed
        # at an index that is different from its hash

    # this function calculates the hash of the given key
    def get_hash(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.MAX

    def len(self):
        return self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key: # If at the given hash (index), at the first element of the inner list,
            # the value equals to key, return what's stored in the next element of the inner list
            return self.arr[h][1]

        new_index = (h + 1) % self.len() # We are using the modulo here to avoid an infinit loop
        # we are confining every index in the range self.len()

        while not (new_index == h): # when the new index is equal to the hashed value, we know that the key
            #  we are looking for is not in the table since this signifies that we have 
            # traversed the whole table and we are back where we started

            if self.arr[new_index][0] == key:
                return self.arr[new_index][1]
            new_index = (new_index + 1) % self.len() # increment new_index by 1 and keep in in the range

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        if self.arr[h][0] == None: # if the first element of the list (where the key should be stored)
            # is None, then that index has not been filed
            self.arr[h][0] = key
            self.arr[h][1] = value

            return # we have done what we wanted so get out of the function

        print("Collision detected") # the hashed index is already filled

        new_index = (h + 1) % self.len() # start probing for the next empty slot
        while not (new_index == h):  # stop when you reach where we started, the table is full   
            if self.arr[new_index][0] == None:
                self.arr[new_index][0] = key
                self.arr[new_index][1] = value
                break
            new_index = (new_index + 1) % self.len()
            if new_index == h:
                print("Table full, cannot insert new item")
            
        
        

    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key:
            self.arr[h][0] = None
            self.arr[h][1] = None
            return
        
        new_index = (h + 1) % self.len()

        while not (new_index == h):
            if self.arr[new_index][0] == key:
                self.arr[new_index][0] = None
                self.arr[new_index][0] = None
                return
            new_index = (new_index + 1) % self.len()


hasht = HashMap()

hasht["march 17"] = 7
hasht["march 26"] = 8
hasht["march 30"] = 34
hasht["march 6"] = 35
hasht["march 20"] = 36
hasht["march 10"] = 80


print(hasht["march 10"])
del hasht["march 10"]
pprint.pprint(hasht.arr)