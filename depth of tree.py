
def depth(P):
   hashTable = {}
   maxDepth = 0
   for i in range(len(P)):
      iDepth = 1
      while(P[i] != -1):
         if hashTable[P[i]] != None:
            iDepth += hashTable[P[i]]
            break
         else:
            iDepth += 1
            i = P[i]
      hashTable[i] = iDepth
      maxDepth = max(iDepth,maxDepth)
   return maxDepth

print (depth([-1,0,0,0,2,2,5,6,6,8,8,8]))

      
      
