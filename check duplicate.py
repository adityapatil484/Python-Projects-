""" Given an array, find duplicate"""


l1 = [3,2,1,2,2,3]

def checkDups(A):
   for i in range(len(A)):
      if A[abs(A[i])] < 0:
         return True
      A[abs(A[i])] = -A[abs(A[i])]
   return False

print(checkDups(l1))
