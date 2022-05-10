"""
This implementation of the stack if from the hardcoded singly linked list.
The items will be inserted/pushed at and deleted/popped from the beggining of the linked list,
that is at the head.
"""

# the Node class is the one that is used to create an object that
#  holds each data item, maintaining a pointer to the next data object
class Node:
    def __init__(self):
        self.data = 0    # to hold the actual data
        self.next = None    # to keep track of the next data object

class Stack:
    def __init__(self):
        self.head = None    # the top of the stack
        self._size = 0  # stack size
    
    def push(self, data):
        dataItem = Node()
        dataItem.data = data
        if self.head is None:   # point the top of the stack to this first item
            self.head = dataItem
            self._size += 1 # The stack size has increased by one
        else:   # let this data item's next pointer point to the current top of the stack
            dataItem.next = self.head
            self.head = dataItem    # update top of the stack to the new data item
            self._size += 1 

    
    def pop(self):
        if self.head == None:   # stack is empty
            raise ValueError("Cannot pop an empty stack")
        data = self.head.data   # temporarily store the data at the top of the stack
        self.head = self.head.next  # move the head to the data idem one step down the stack, leaving the data object
        # that was once pointed to by self.head unreferenced and ellegible for garbage collection 
        self._size -= 1 # reduce the size of the stack by one
        return data
    
    def peek(self):
        if self.head == None:
            raise ValueError("Stack is empty")
        return self.head.data
    
    def length(self):
        return self._size

    def is_empty(self):
        return self.head==None
    
