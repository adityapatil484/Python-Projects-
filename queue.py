import random
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
 
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enQueue(self, data):
        node = Node(data)
        if self.front is None:
        	self.front = node 
        	self.rear = node
        self.rear.next = node
        self.rear = node
 
    def deQueue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
        	self.rear = None
        return temp.data
    def peakFront(self):
        return self.front   
random.seed(2)
queue = Queue()
for i in range(5):
    element = random.randint(0, 99)
    print ("Enqueueing:", element)
    queue.enQueue(element)
 
print (queue.deQueue())
