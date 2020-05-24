import random
class Stack:
    def __init__(self, Capacity=5):
        self.array = []
        self.capacity = Capacity
    def push(self, data):
        if len(self.array) < self.capacity:
            self.array.append(data)
        else:
            print ("Stack Overflow")
    def pop (self):
        if self.isEmpty():
            print("Underflow")
            return
        return self.array.pop()
    def peak(self):
        if self.isEmpty():
            print ("Underflow")
            return        
        return self.array[-1]     
    def size(self):
        return len(self.array)
    def isEmpty(self):
        if len(self.array) == 0:
            return True
        return False
 
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    def enQueue(self, data):
        self.s1.push(data)
    def deQueue(self):
        if not self.s2.isEmpty():
            return self.s2.pop()
        while(not self.s1.isEmpty()):
            self.s2.push(self.s1.pop())
        return self.s2.pop()
 
queue = Queue()
queue.enQueue(21)
queue.enQueue(519)
print (queue.deQueue())
