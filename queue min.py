import random

class Stack:
   
   def __init__(self, Capacity):
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
 
class AdvStack:
   
   def __init__(self):
      self.eStack = Stack()
      self.minStack = Stack()
      
   def push(self, data):
      self.eStack.push(data)
      if self.minStack.size() == 0 or data <= self.minStack.peak():
         self.minStack.push(data)
         
   def pop(self):
      temp = self.eStack.pop()
      if temp == self.minStack.peak():
         self.minStack.pop()
      return temp
   
   def getMin(self):
      return self.minStack.peak()
