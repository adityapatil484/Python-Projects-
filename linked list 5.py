class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
 
class LinkedList:
    def __init__(self, node=None):
        self.head = node
    def checkCycle(self):
        fp = self.head
        sp = self.head
 
        while(fp):
            fp = fp.next
            if fp == sp:
            	return True
            if fp:
            	fp = fp.next
            else:
            	return False
            sp = sp.next
            if fp == sp:
            	return True            
        return False
    def findCycleLength(self):
        fp = self.head
        sp = self.head
 
        while(fp):
            fp = fp.next
            if fp == sp:
            	break
            if fp:
            	fp = fp.next
            else:
            	return 0
            sp = sp.next
            if fp == sp:
            	break
        if fp is None:
        	return 0
        c = 0
        fp = fp.next
        while sp != fp:
        	c += 1
        	fp = fp.next
        return c
 
n1 = Node(10);n2 = Node(1);n3 = Node(519);n4 = Node(9);n5 = Node(11);
n6 = Node(16);n7 = Node(321);n8 = Node(451);n9 = Node(31);n10 = Node(109)
n1.next=n2;n2.next=n3;n3.next=n4;n4.next=n5;n5.next=n6;
n6.next=n7;n7.next=n8;n8.next=n9;n9.next=n10;n10.next=n7
 
ll = LinkedList(n1)
print (ll.findCycleLength())
