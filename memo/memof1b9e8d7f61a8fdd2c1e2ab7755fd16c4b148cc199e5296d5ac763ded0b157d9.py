def gen_primes(N):
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n


def gen_primes(N):
    primes = []
    for n in range(2, N):
        if all(n % p for p in primes):
            primes.append(n)
    return primes


print(gen_primes(10))


def gen_primes(N):
    cache = []
    for i in range(2, N):
        if all(i % n for n in cache):
            cache.append(i)
    return cache


print(gen_primes(50))


def divisor(N):
    result = []
    for i in range(2, N):
        if N % i == 0:
            return False
    return True


def prime_til(N):
    result = []
    for i in range(2, N):
        if divisor(i):
            result.append(i)
    return result


print(prime_til(50))


print((2**3) * (3**2))

(print(all([1, 2, 3])))

print(*gen_primes(90))

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
