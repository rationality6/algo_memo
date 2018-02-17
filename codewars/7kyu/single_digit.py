# The goal of this Kata is to reduce the passed integer to a single digit (if not already) by converting the number to binary, taking the sum of the binary digits, and if that sum is not a single digit then repeat the process.
#
# n will be an integer such that 0 < n < 10^20
# If the passed integer is already a single digit there is no need to reduce
# For example given 5665 the function should return 5:


class Test:
    def assert_equals(a, b):
        print(a == b)


# def single_digit(N):
#     import re
#     isBinary = re.compile(r'^[01]+$').match(str(N))
#     if(isBinary):
#         if(N > 10**20):
#             return sum([int(i) for i in list(str(N)) if i == '1'])
#         else:
#             return int(str(N), 2)
#     else:
#         return int(bin(N)[2:])


def single_digit(N):
    while N > 9:
        N = sum([int(i) for i in bin(N)[2:] if i == '1'])
    return N


# def single_digit(n):
#     while n > 9:
#         print(n)
#         n = bin(n).count("1")
#     return n


Test.assert_equals(single_digit(5665), 5)
Test.assert_equals(single_digit(16), 1)
