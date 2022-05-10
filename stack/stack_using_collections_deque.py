""" 
Implementation of the stack data structure using the collections.deque as a base/container data structure.

Stack data structure is a Last In First Out (LIFO) data structure; which eans that
the last item to be inserted is the first item to come out of the stack.
The stack data structure supports the push operation which pushes/inserts a data 
item at the top of the stack, the pop operation which removes the data item at the top of the stack 
(the last item pushed on the stack) and the peek operation that only returns the item at the top
of the stack, but unlike pop, it does not remove it.

I've added the length and tge is_empty function to return the size of the stack and if it is empty respectively
"""

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, item):
        return self.container.append(item)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1] 
    
    def is_empty(self):
        return len(self.container)==0

    def length(self):
        return len(self.container)

