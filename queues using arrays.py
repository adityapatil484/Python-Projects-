import random
class Queue:
    def __init__(self, Capacity):
        self.array = []
        self.capacity = Capacity
    def enQueue(self, data):
    	if len(self.array) < self.capacity:
    		self.array.append(data)
    	else:
    		print "Queue Overflow"
    def deQueue(self):
        if self.isEmpty():
        	print "Underflow"
        	return
        return self.array.pop(0)
    def peak(self):
        if self.isEmpty():
        	print "Underflow"
        	return    	
        return self.array[0]     
    def size(self):
        return len(self.array)
	def isEmpty(self):
		if len(self.array) == 0:
			return True
		return False
