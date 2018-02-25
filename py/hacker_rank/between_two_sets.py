# You will be given two arrays of integers. You will be asked to determine all integers that satisfy the following two conditions:
#
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
#
# Input Format
#
# The first line contains two space-separated integers describing the respective values of , the number of elements in array , and , the number of elements in array .
# The second line contains  distinct space-separated integers describing .
# The third line contains  distinct space-separated integers describing .
#
# Constraints
#
# Output Format
#
# Print the number of integers that are considered to be between  and .
#
# Sample Input
#
# 2 3
# 2 4
# 16 32 96
# Sample Output
#
# 3
# Explanation
#
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
#
# 4, 8 and 16 are the only three numbers for which each element of A is a factor and each is a factor of all elements of B.
#


class test():
    def assert_equals(a, b):
        print(a == b)


def solution(left, right):
    print(left[0], right[-1])


list0 = [2, 3]
list1 = [16, 32, 96]
solution(list0, list1)


def get_factors(N):
    result = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            result.extend([i, N // i])
    return set(result)


a = get_factors(32)
a = get_factors(32)


from functools import reduce


def factors(n):
    # return reduce(list.__add__,
    #                   ([i, n // i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))


def get_gcd()


def factors(N):
    import math
    result = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            result.extend([i, N // i])
    return set(result)


print(factors(32))

import math
print(math.sqrt(24))
print(24**0.5)


def get_prime(N):
    result = set()
    for i in range(2, N):
        if all(i % j > 0 for j in result):
            result.add(i)
    return result


print(get_prime(32))


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)
