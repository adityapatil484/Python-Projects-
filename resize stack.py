import random
class Stack:
    def __init__(self, Capacity):
        self.array = []
        self.capacity = Capacity
    def push(self, data):
        if len(self.array) == self.capacity:
            self.resize()
        self.array.append(data)
 
    def pop (self):
      temp = self.array.pop()
      if len(self.array) <= (self.capacity//2):
         self.resize()
         return temp
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
    def resize(self):
        if len(self.array) == self.capacity:
            self.capacity *= 2
            self.array = list(self.array)
        if len(self.array) < (self.capacity//2):
            self.capacity = self.capacity//2
            self.array = list(self.array)
    def getCapacity(self):
        return self.capacity
random.seed(2)
stack = Stack(1)
for i in range(5):
    element = random.randint(0, 99)
    stack.push(element)
 
print (stack.size())
print (stack.getCapacity())
stack.pop()
stack.pop()
 
print (stack.size())
print (stack.getCapacity())
