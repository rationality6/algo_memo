# down to top
def fib(n):
    arr = [1, 1]
    for i in range(2, n):
        arr.insert(i, arr[i - 2] + arr[i - 1])
    print(arr[n - 1])
fib(10)

#down to top
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(a)
fib(10)

#down to top
def fib(n, a=0, b=1):
    l = [0]
    for _ in range(n):
        a, b = b, a + b
        l.append(a)
    return l
print(fib(10))

# top to bottom
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10))


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

from itertools import count
for i in count():
    print(i, end=' ')
    if i >= 10:
        break

from itertools import count
factors = [2, 3, 5, 7]
G = (i for i in count() if all(i % n > 0 for n in factors))

for val in G:
    print(val, end=' ')
    if val > 40:
        break

factors = [2, 3, 5, 7]
for n in factors
print(all(i <= 9 for i in range(10)))

L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')
print()
for val in L:
    print(val, end=' ')

G = (n ** 2 for n in range(12))
print(list(G))
print(list(G))


G = (n ** 2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30:
        break

print("\ndoing something in between")

for n in G:
    print(n, end=' ')


def memoization(num):
    memo_map = {0: 0, 1: 1}
    if in map_map
        memo_map[num] = memoization(num - 1) + memoization(num - 2)
    return memo_map[num]


print(memoization(20))


import time
st = time.time()

cache = {}


def fib(n):
    if n not in cache.keys():
        cache[n] = _fib(n)
    return cache[n]


def _fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(_fib(15))
# print(fib(15))

print("{}".format(time.time() - st))
