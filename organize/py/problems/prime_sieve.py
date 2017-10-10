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

print(*gen_primes(90))
