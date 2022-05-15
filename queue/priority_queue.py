"""
A priority queue data structure is a queue that ranks data items according to their priorities.
If a data item has a priority of 1, it is processed first before the one with a priority of 4,
even if it got into the queue after the one with priority 4. One of the examples where
priority  queues are applicable is in the process scheduler. If a user process with priority 2 is in the scheduler, 
waiting for the CPU and a system process with priority -1 enters the queue,
the system process is given the CPU first since its priority is greater than that of the user process.

To come up with this type of data structure, where insertion/enqueuing is done at the beginning of the queue,
and queueing at the end, using a doubly linked list to implement it allows us to handle queueing without
touching the head, unless the head equals the tail.

Queueing is done in constant time O(1), but enqueuing now has the worst case time complexity of O(n).
"""


class DataItem:
    def __init__(self):
        self.data = 0
        self.priority = 0
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self._size = 0

    def enqueue(self, data, priority):
        data_item = DataItem()
        data_item.data = data
        data_item.priority = priority
        if self.is_empty():
            self.head = self.tail = data_item

        elif data_item.priority > self.head.priority:
            self.head.prev = data_item
            data_item.next = self.head
            self.head = data_item

        elif data_item.priority < self.head.priority:
            temp = self.head
            while temp.priority > data_item.priority and temp != self.tail:
                temp = temp.next
            if temp != self.tail or data_item.priority > self.tail.priority:
                data_item.next = temp
                temp.prev.next = data_item
                data_item.prev = temp.prev
                temp.prev = data_item
            else:
                temp.next = data_item
                data_item.prev = temp
                self.tail = data_item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is currently empty")
            return
        (dequeued, pr) = self.tail.data, self.tail.priority
        self.tail = self.tail.prev
        self.tail.next = None
        self._size -= 1
        return dequeued, pr

    def length(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def peek(self):
        return (self.tail.data, self.tail.priority) if not self.is_empty() else "Queue is empty"


"""
# ____________________________________________________________________________
# Test drive

p_queue = Queue()

print(p_queue.length())
print(p_queue.is_empty())
print(p_queue.peek())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

p_queue.enqueue(54, 2)
p_queue.enqueue(50, 9)
p_queue.enqueue(53, 0)
p_queue.enqueue(51, 1)
p_queue.enqueue(54, 7)
p_queue.enqueue(45, 2)
p_queue.enqueue(35, 4)
p_queue.enqueue(87, 3)
p_queue.enqueue(32, 10)
p_queue.enqueue(56, -1)
p_queue.enqueue(12, 11)
p_queue.enqueue(100, -2)
p_queue.enqueue(112, 3)
p_queue.enqueue(111, -2)
p_queue.enqueue(120, 4)


print(p_queue.length())
print(p_queue.is_empty())
print(p_queue.peek())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Cleaning time.................")

print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print(p_queue.length())
print(p_queue.is_empty())
print(p_queue.peek())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Again .....")

print(p_queue.dequeue())
print(p_queue.dequeue())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print(p_queue.length())
print(p_queue.is_empty())
print(p_queue.peek())
"""
