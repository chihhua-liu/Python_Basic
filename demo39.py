# demo39   math & random

import math
import random

print(math.pi, math.e)
for _ in range(10):
    print(random.randint(5, 10), end=" ")
print()

stores = ['7-11', 'fami', 'mos', 'macdonald']
for _ in range(5):
    print(random.choice(stores))    #random choice one of list


cards = ['A', 'K', 'Q', 'J', '10']  #random reorganize   list
for _ in range(10):
    random.shuffle(cards)
    print(cards)