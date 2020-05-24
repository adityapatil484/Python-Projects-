class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node
    def length(self):
        current = self.head
        c = 0
        while(current != None):
            c += 1
            current = current.next
        return c
    def printList(self):
        current = self.head
        while(current != None):
            print (current.data)
            current = current.next
    def search(self, data):
        current = self.head
        while(current != None):
            if (current.data == data):
                return current
            current = current.next            

    def insertAtBegin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while(current.next != None):
            current = current.next    
        current.next = node
    def insert(self, position, data):
        if position <= 1:
            self.insertAtBegin(data)
            return
        node = Node(data)
        c = 1
        current = self.head
        while(current != None and c < position-1):
            current = current.next
            c += 1
        if current is None:
            self.insertAtEnd(data)
            return
        node.next = current.next
        current.next = node
    def insert2(self, position, data):
        node = Node(data)
        if position <= 1:
            node.next = self.head
            self.head = node
            return

        c = 1
        current = self.head
        while(current != None and c < position-1):
            current = current.next
            c += 1
        if current is None:
            self.insertAtEnd(data)
            return
        node.next = current.next
        current.next = node
    def deleteFromBegin(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
        return temp
    def deleteFromEnd(self):
        current = self.head
        while(current.next != None):
            prev = current
            current = current.next
        prev.next = None
        return current
    def delete(self, position):
        if position <= 1:
            if self.head:
                temp = self.head
                self.head = self.head.next
                return temp

        c = 1
        current = self.head
        while(current != None and c < position-1):
            current = current.next
            c += 1
        if current is None:
            return None
        temp = current.next
        current= current.next.next
        return temp
ll = LinkedList()
ll.insertAtEnd(5)
ll.insertAtEnd(55)
ll.insertAtBegin(10)
ll.insert(1, 99)
ll.insert(3, 6)
result = ll.delete(4)
#ll.printList()
if result:
    print (result.data)
