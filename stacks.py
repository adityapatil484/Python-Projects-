import random
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
 
class Stack:
    def __init__(self, node=None):
        self.top = node
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
    def pop (self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
   
random.seed(2)
stack = Stack()
 
for i in range(10):
    element = random.randint(0, 99)
    print ("Pushing:", element)
    stack.push(element)
 
for i in range(10):
    print ("Popping:", stack.pop())
