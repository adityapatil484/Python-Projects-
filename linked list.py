# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:18:58 2019

@author: Adi
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.Next = None

class LinkedList():
    def __init__(self, node=None):
        self.top = node
        
    def printList(self):
        current = self.top
        while current != None:
            print(current.data, end = " --> ")
            current = current.Next
        print(None)
            
    def addtotop(self, data):
        node = Node(data)
        node.Next = self.top
        self.top = node
        
    def removefromtop(self):
        self.top = self.top.Next

    def removefromend(self):
        current = self.top
        while current.Next.Next != None:
            current = current.Next
        current.Next = None
        
    def addtoend(self,data):
        node = Node(data)
        current = self.top
        while current.Next != None:
            current = current.Next
        current.Next = node
            
        
l1 = LinkedList()
l1.printList()
l1.addtotop(10)
l1.printList()
l1.addtotop(20)
l1.printList()
l1.addtotop(30)
l1.printList()
l1.removefromtop()
l1.printList()
l1.removefromend()
l1.printList()
l1.addtoend(25)
l1.printList()