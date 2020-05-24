from random import *

deck = [{'value':i,'suit':c}
        for c in ['spades','clubs','hearts','diamonds']
        for i in range(2,15)]


flush = 0

for i in range(10000):
   shuffle(deck)
   if deck[0]['suit'] == deck[1]['suit'] and deck[0]['suit'] == deck[2]['suit'] and deck[0]['suit'] == deck[3]['suit'] and deck[0]['suit'] == deck[4]['suit']:
         flush = flush + 1

print(flush/10000)




