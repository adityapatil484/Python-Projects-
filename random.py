import random

l= [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (10000):
    a= random.randint(1,6)
    b= random.randint(1,6)
    c = a + b
    l[c-1] +=1
print(l[1:])


for i in range (len(l)):
    l[i] = (l[i]/10000)*100
    
print(l[1:])
    
