# import hashlib
# print(hashlib.sha256(b"??").hexdigest())

import itertools
p = itertools.permutations(range(3))
print(*p)

import itertools
c = itertools.combinations(range(4), 2)
print(*c)

from itertools import product
p = product('ab', range(3))
print(*p)

from itertools import product
p = product('ab', range(3))
print(*p)

print([i for i in range(20) if i % 3 > 0])

L = []
for n in range(12):
    L.append(n ** 2)
print(L)

print([n ** 2 for n in range(12)])

print([n**2 for n in range(12)])

print([(i, j)for i in range(2)for j in range(3)])

[val for val in range(20) if val % 3 > 0]

print("{}*{}={}\n".format(i, y, i * y) for i in range(10) for y in range(10))

print([val for val in range(20) if val % 3 > 0])

L = []
for val in range(20):
    if val % 3:
        L.append(val)
print(L)

val = -10
print(val if val >= 0 else -val)
print(1 if False else 2)

print([*range(20)])

import numpy as np
a0 = [[1, 2], [3, 4]]
b0 = [[5, 6], [7, 8]]
z = (np.array(a0)) + (np.array(b0))
print(z)

import numpy as np

a0 = [[1, 2], [3, 4]]
b0 = [[5, 6], [7, 8]]

result = []
for a, b in zip(a0, b0):
    result.append([c + b for c, b in zip(a, b)])
print(result)

print([val if val % 2 else -val for val in range(20) if val % 3])


print({n: n**2 for n in range(6)})
a = (n**2 for n in range(12))
print(*a)

a = [(n ** 2 for n in range(12))]

print(*a[0])

G = (n ** 2 for n in range(12))
print(list(G))


[n ** 2 for n in ragne(12)]

G = (n ** 2 for n in range(12))
print(G)

G = (n ** 2 for n in range(12))
for val in G:
    print(val, end=' ')

from itertools import count
print(count())

for i in count():
    print(i, end='')
    if i >= 10:
        break

factors = [2, 3, 5, 7]
G = (i for i in count())


factors = [2, 3, 5, 7]
factors[factors.index(max(factors))] -= 1
factors[factors.index(max(factors))] -= 1
factors[factors.index(max(factors))] -= 1
print(factors)

L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')

G = (n**2 for n in range(12))
for val in G:
    print(val, end=' ')
