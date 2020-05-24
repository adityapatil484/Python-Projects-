from functools import reduce

l1 = [1,2,3,4,5]

factorial = reduce (lambda x,y: x*y, l1)

print(factorial)
