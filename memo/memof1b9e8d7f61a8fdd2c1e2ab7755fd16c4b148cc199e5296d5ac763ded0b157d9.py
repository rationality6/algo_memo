# import hashlib
# a = hashlib.sha256(b"oxf").hexdigest()
# print(a)
#
# L1 = [n**2 for n in range(12)]
# L2 = []
#
# for n in range(12):
#     L2.append(n**2)
#
# print(L1)
# print(L2)
#
#
# G1 = (n ** 2 for n in range(12))
#
#
# def gen():
#     for n in range(12):
#         yield n ** 2
#
#
# G2 = gen()
# print(*G1)
# print(*G2)
#
# L = [n for n in range(2, 40)]
# print(L)
#
# L = [n for n in L if n == L[0] or n % L[0] > 0]
# print(L)
#
# L = [n for n in L if n == L[1] or n % L[1] > 0]
# print(L)
#
# L = [n for n in L if n == L[2] or n % L[2] > 0]
# print(L)
#
# primes = set()
# s = {1, 2, 3, 4, 5, 6}
# s.add(7)
# print(s)
#
# a = [*range(3)]
# print(a)
# while a:
#     print('foo')
#     a.pop()


# def gen_primes(N):
#     primes = set()
#     for n in range(2, N):
#         print(n)
#         print(primes)
#         if all(n % p > 0 for p in primes):
#             primes.add(n)
#             yield n


def gen_primes(N):
    primes = set()
    for n in range(2, N):
        if all(n % p for p in primes):
            primes.add(n)
            yield n


print(*gen_primes(70))

print(all([i < 4 for i in range(5)]))

from functools import reduce

print(reduce(lambda a, b: a + b, range(11)))


import math
print(math.cos(math.pi))


import numpy as np
print(np.cos(np.pi))

from math import *
print(sin(pi) ** 2 + cos(pi)**2)

help(sum)

print(sum(range(5), -1))
print(sum(range(5)))

from numpy import *
print(sum(range(5), 3))

print(sum(range(0, 5)))
print(sum([1, 2, 3, 4]))
print(range(0, 5))


fox = "tHe qUICk bROWn fOx."
print(fox.swapcase())
line = '     this is the content      '
print(line.rstrip())


num = "0000000004305"
print(num.strip('0'))
print(num.center(20))


for i in range(1, 20, 2):
    print((i * '*').center(29))

line = "this is the content"
print(line.rjust(30))

print('453'.rjust(10, '0'))
print('435'.zfill(10))

line = 'the quick brown fox jumped over a lazy dog'
print(line.find('fox'))

line = 'the dog quick brown fox jumped over a lazy dog'
print(line.rfind('a'))
line = 'the quick brown fox jumped over a lazy dog'
print(line.startswith('he'))
print(line.find('bear'))

line = 'the quick brown fox jumped over a lazy dog'
print(line.split())
print(line.partition('over'))

print('--'.join(['1', '2']))

haiku = """matsushima-ya
aah matsushima-ya
matsushima-ya"""

print(haiku.splitlines())

pi = 3.15159
print("pi = {0:.3f}".format(pi))

!ls * Python * .ipynb


import re
line = 'the quick brown fox jumped over a lazy dog'
regex = re.compile('\s+')
print(regex.split(line))
