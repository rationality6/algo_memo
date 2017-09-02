def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))

from functools import reduce


def factorial(n): return reduce(lambda x, y: x * y, [1] + range(1, n + 1))


print(factorial(10))

import math
print(math.factorial(4))


print(1*2*3*4*5)
