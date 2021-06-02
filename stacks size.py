import random
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
 
class Stack:
    def __init__(self, node=None):
        self.top = node
        self.c = 0
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.c += 1
    def pop (self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        self.c -= 1
        return temp.data
    def peak(self):
        return self.top       
    def size(self):
        return self.c
   
random.seed(2)
stack = Stack()
for i in range(5):
    element = random.randint(0, 99)
    print ("Pushing:", element)
    stack.push(element)
 
print (stack.size())
