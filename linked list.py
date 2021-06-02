"""LINKED LIST"""

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
    
    def setdata (self,d):
        self.data = d

    def getdata (self):
        return self.data

    def setNext (self,node):
        self.next = node

    def getNext (self):
        return self.next

node1 = Node(2)
node2 = Node(6)
node3 = Node(10)

node1.setNext(node2)
node2.setNext(node3)

print (node1.getNext().getdata())





