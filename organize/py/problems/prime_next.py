def is_prime(number):
    import math
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


print(is_prime(50))
print(is_prime(7))


def get_prime(N):
    cache = set()
    for i in range(2, N):
        if all(i % z for z in cache):
            cache.add(i)
    return cache


print(get_prime(100))

import math
for i in range(3, int(math.sqrt(50) + 1), 2):
    print(i)


is_prime(7)


def simple_generator_function():
    yield 1
    yield 2
    yield 3
    yield 4


for val in simple_generator_function():
    print(val)


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


get_primes(7)





import itertools
mylist = [1, 2, 3]
mypermuatation = itertools.permutations(mylist)
for i in mypermuatation:
    print(i)


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


print([*all_perms([1, 2, 3])])

for i in all_perms([1, 2, 3]):
    print(i)


for i in range():
    print(i)


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


for i in permutations([1, 2, 3]):
    print(i)
