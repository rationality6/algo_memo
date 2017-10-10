#
# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
#
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


class test:
    def assert_equals(a, b):
        # print(a)
        pass


def primeFactors(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret


def primeFactors(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while (n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += "({}{})".format(i, "**%d" % num if num > 1 else "")
        if n == 1:
            return ret


print(primeFactors(12))
print(primeFactors(199))
test.assert_equals(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")


def gen_primes(N):
    primes = set()
    for i in range(2, N):
        if all(i % p > 0 for p in primes):
            primes.add(i)
            yield i

# def foo(n):
#     for i in range(2, n+1):
#         n/=i
#         print(i)
#
# foo(12)

# l = [3, 2, 4]
# import itertools
# p = itertools.combinations(l, 2)
# print([*p])

# 6
