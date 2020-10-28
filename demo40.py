# demo40

import itertools

a1 = ['A', 'C', 'E']
a2 = [6, 7, 8, 9]
a3 = ['a', 'b', 'c', 'd', 'e']
result = itertools.chain(a1, a2, a3)
print(type(result), result)
for item in result:
    print(item, end=" ")
print()
print("------------------------------------------------")

print('print again')
for item in result:
    print(item, end=" ")
print("------------------------------------------------")
result2 = tuple(itertools.chain(a1, a2, a3))
print(result2)
print(result2)
print("------------------------------------------------")
p1 = tuple(itertools.permutations(a3, 2))
print(len(p1), p1)
print("------------------------------------------------")
c1 = tuple(itertools.combinations(a3, 2))
print(len(c1), c1)