# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:39:01 2019

@author: Adi
"""

class Queue:
    def __init__(self):
        self.items = []
        
    def add(self,data):
        self.items.append(data)
        
    def remove(self):
        if  (len(self.items)==0):
            print('Empty Queue')
        else:
            return (self.items.pop(0))
            
    def __str__(self):
        queue = ''
        for i in range(len(self.items)):
            if i == len(self.items)-1:
                queue += str(self.items[i]) 
                continue
            queue += str(self.items[i]) + '<--'
        return (queue)

myqueue = Queue()
myqueue.add(10)
myqueue.add(15)
myqueue.add(20)
myqueue.add(25)
print(myqueue)
x = myqueue.remove()
print(x)
print(myqueue)