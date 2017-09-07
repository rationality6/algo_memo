import hashlib
m = hashlib.sha256().hexdigest()
print(m)


def separator(mid, til):
    lower = []
    upper = []

    for i in range(1, til + 1):
        upper.append(i) if i > mid else lower.append(i)

    return (lower, upper)


result = separator(5, 10)
print(result)

x = 1 + 2 + 3 + 4 + \
    5 + 6 + 7 + 8
print(x)

x = (1 + 2 + 3 + 4 +
     5 + 9)
print(x)

print(7 | 4)

x = [1, 2, 3]
y = x
y.append(4)
print(x)
y = "something else"
print(x)
print(y)

x = 10
y = x
x = x + 5
print(x)
print(y)


x = 4
print(type(x))
x = "hello"
print(type(x))
x = 3.14159
print(type(x))

x = 4.5
print(x.real, "+", x.imag, 'i')

x = 4.5
print(x.is_integer())
x = 4.0
print(x.is_integer())


print(7.0 // 8)

a = [[1., 2.], [3., 4.]]
b = [[3., 4.], [3., 4.]]
print(a @ b)

import numpy as np
a = [[1, 2], [3, 4]]
b = [[3, 4], [3, 4]]
c = np.matmul(a, b)
print(c)

print(bin(255))
print(bin(4))
print(bin(10))
print(4 | 10)
print(4 ^ 3)

a = False
b = True

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

print(1 in range(0, 2))

j = 3
x = 1 + 2j
print(x)

x = 1
print(type(x))

print(2**200)

import numpy as np
a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4]]
na = np.array(a)
print(a)
nb = np.array(b)
print(b)
print(na + nb)


print("0.1 = {0:.17f}".format(0.1))
print("0.1 = {0:.17f}".format(0.2))
print("0.1 = {0:.17f}".format(0.3))

10011001100110011001100
10011001100110011001101
print(len("10011001100110011001101"))

print(complex(1, 2))

print(0.1 + 0.2)


def foo():
    print("foo")


print(foo())


import collections


def solution(v):
    answer = []

    for a in zip(*v):
        b = collections.Counter(a)
        for i in b:
            if b[i] == 1:
                answer.extend([i])

    return answer


v = [[1, 4], [3, 4], [3, 10]]
v2 = [[1, 1], [2, 2], [1, 2]]


print(solution(v))
print(solution(v2))

l = [1, 'two', 3.14, [0, 3, 5]]
print(l)


l = [2, 3, 5, 7, 11]
l[1:3] = [55, 56]
print(l)

t = (1, 2, 3)
t = 1, 2, [3, 3, 'foo']
print(t)

x = 0.125
n, d = x.as_integer_ratio()
print(n / d)

numbers = {
    'one': 1,
    'two': 2,
    'three': 3
}

numbers['ninety'] = 90

print(numbers)

primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
print(primes | odds)
print(primes.union(odds))

primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
print(primes & odds)
print(primes.intersection(odds))

primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
print(primes - odds)
print(odds - primes)
print(primes.difference(odds))


primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
print(primes ^ odds)
print(primes.symmetric_difference(odds))

import collections

a = collections.OrderedDict({1: 1, 1: 1, 1: 1, })
print(a)

import collections

a = collections.Counter([1, 2, 3, 3, 3])
print(a)
