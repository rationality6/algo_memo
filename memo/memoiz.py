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
fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


def sum_fib(n):
    return sum(math.factorial(i)for i in fib_list[:n])


print(sum_fib(10))


def get_prime(til):
    primes = []
    for i in range(2, til):
        while all(i % z > 0 for z in primes):
            primes.append(i)
    return primes


print(get_prime(30))


def test(n):
    primes_answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                     97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    print(len(primes_answer))
    if n == primes_answer[:len(n)]:
        return True
    else:
        return False


print(test(get_prime(50)))
