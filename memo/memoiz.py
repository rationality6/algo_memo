def fib(N):
    result = [0, 1]
    for i in range(2, N):
        result.append(result[i - 1] + result[i - 2])
    return result
print(fib(22))

def factorial(N):
    if N <= 1:
        return N
    else:
        return N * factorial(N - 1)

import math
fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
def sum_fib(n):
    return sum(math.factorial(i)for i in fib_list[:n])
print(sum_fib(10))
