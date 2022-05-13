"""
Implementation of a queue data structure using singly linked list.
A queue is a first in first out (FIFO) data structure, an item that was inserted
first is also the first to come out.

A real life example of a queue is the queue at a bank where the first person 
to enter into the queue is the first to be served hence the first to get out 
of the queue. In this implementation, insertion/pushing is done at the end of the queue and 
deletion/ popping is done at the beginning of the queue. To allow our queue to be efficient,
it will maintain the heard and the tail pointers in order to allow for fast pop and push respectively. 
Insertion should be done at a constant time (O(1)) as well as deletion. To maintain this property,
the tail pointer points to the end of the queue and will be updated accordingly at insertion,
otherwise insertion would take O(n) since we would have to traverse through each element
in the list from the head until we reach the last data item in the queue. Also, finding the size of the queue would take O(n), but updating the counter of data items time
we add a new data item allows us to achieve a constant time access.

Peeking and checking whether the queue is empty are always in O(1).
"""

class DataItem:
    def __init__(self):
        self.data = 0
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = self.head   # Initially, the head and the tail pont to the same location
        self._size = 0  # Initially the queue is empty
    
    def length(self) ->int:
        return self._size
    
    def push(self, data:int)->None:
        # First create a data item object
        data_item = DataItem()
        data_item.data = data
        # Then add it to the queue
        if self.is_empty():
            self.tail = self.head = data_item
            self._size += 1 # Increment the size of the queue with each insertion
        else:
            self.tail.next = data_item # Insertion is at the end of the queue
            self.tail = data_item
            self._size += 1
    
    def pop(self) ->DataItem().data:
        # first check if the stack is not empty before popping
        if self.is_empty():
            print("The queue is empty!")
            return
        data = self.head.data
        self.head = self.head.next  # head now point to the next data item
        self._size -= 1 # decrement the queue size with every deletion
        return data

    def is_empty(self)->bool:
        return True if self.head == None else False
    
    def peek(self)->DataItem().data:
        if self.is_empty():
            print("The queue is empty!")
            return
        return self.head.data   # return the data item that is elegible for a pop

#______________________________________________________________________________

#   Test drive

queue = Queue()

queue.pop()
print(queue.length())
print(queue.is_empty())
print("============================================================================")
queue.push(11)
queue.push(12)
queue.push(13)
queue.push(14)
queue.push(15)
queue.push(16)
queue.push(17)
queue.push(18)

print(queue.length())
print(queue.is_empty())
print(queue.peek())

print("============================================================================")

print("Pop time ...")
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())

print("============================================================================")

print(queue.length())
print(queue.is_empty())
print(queue.peek())
