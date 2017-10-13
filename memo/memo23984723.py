
def get_prime(N):
    primes = []
    for i in range(2, N + 1):
        if all(i % z > 0 for z in primes):
            primes.append(i)
    return primes[-1]


print(get_prime(29))


def isPrime(N):
    return N == get_prime(N)


print(isPrime(29))
