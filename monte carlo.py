import random

dice1 = 0
dice2 = 0

result = [0 for i in range(13)]



for i in range(10000):
   
   dice1 = random.randint(1,6)
   dice2 = random.randint(1,6)
   sum = dice1 + dice2
   result[sum] = result[sum] + 1

for i in range(13):
   print((result[i]/10000)*100)



