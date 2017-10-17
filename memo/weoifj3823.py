class Test:
    def assert_equals(a, b):
        print(a)
        print(a == b)

    def it(S):
        print(S)


def get_prime(a, b):
    primes = []
    for i in range(2, b):
        if all(i % z > 0 for z in primes):
            primes.append(i)
    return [i for i in primes if i >= a]


# def solve(a, b):
#     prime_arr = get_prime(a, b)
#     print(prime_arr)
#     result = 0
#     for i in range(a, b_:
#         if i in prime_arr:
#             result += prime_arr[i - 1]
#     return result

def sieve(b):
    primes = []
    for i in range(2, b):
        if all(i % z > 0 for z in primes):
            primes.append(i)
    return primes

def solve(a, b):
    primes=sieve(b)
    n=1
    total=0
    for i in range(2, b + 1):
        if primes[i]:
            if i >= a and primes[n]:
                total += i
            n += 1
    return total

Test.it("Basic tests")
Test.assert_equals(solve(0, 10), 8)
Test.assert_equals(solve(2, 200), 1080)
Test.assert_equals(solve(200, 2000), 48132)
# Test.assert_equals(solve(500, 10000), 847039)
# Test.assert_equals(solve(4000, 450000), 806250440)
