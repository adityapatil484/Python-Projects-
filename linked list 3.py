class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
 
class LinkedList:
    def __init__(self, node=None):
        self.head = node
    def middle(self):
        v = self.head
        r = self.head
        while(v):
            v =  v.next
            r = r.next
            if v:
                v = v.next
        return r
    def middle2(self):
        v = self.head
        r = self.head
        while(v and v.next):
            v =  v.next.next
            r = r.next
        return r
    def findkth(self, k):
        b1 = self.head
        b2 = self.head
        while(k):
            b1 = b1.next
            k -= 1
        while(b1):
            b1 = b1.next
            b2 = b2.next
        return b2
n1 = Node(10);n2 = Node(1);n3 = Node(519);n4 = Node(9);n5 = Node(11);
n6 = Node(16);n7 = Node(321);n8 = Node(451);n9 = Node(31);n10 = Node(109)
n1.next=n2;n2.next=n3;n3.next=n4;n4.next=n5;n5.next=n6;
n6.next=n7;n7.next=n8;n8.next=n9;n9.next=n10
 
ll = LinkedList(n1)
result = ll.findkth(3)
if result:
    print (result.data)
else:
    print ("NONE :(") 
