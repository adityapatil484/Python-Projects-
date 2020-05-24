def func1(x):
   x = x+1
   return x
def func2(L):
   copy = L[:]
   copy.append(0)
   return copy
   
a = 3
M = [1,2,3]
a = func1(a)
func2(M)
print(a)
print(M)
