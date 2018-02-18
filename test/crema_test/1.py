# Complete the function below.


def findNumber(arr, k):
    print(arr)
    print(k)
    return 'YES' if k in arr else "NO"


print(findNumber([5, 1, 2, 3, 4, 5, 1], 1))


def solve(a0, a1, a2, b0, b1, b2):
    arr0 = [a0, a1, a2]
    arr1 = [b0, b1, b2]
    a_score = 0
    b_score = 0

    for x, y in zip(arr0, arr1):
        if(x > y):
            a_score += 1
        elif(x < y):
            b_score += 1
        else:
            pass

    return [a_score, b_score]


print(solve(5, 6, 7, 3, 6, 10))


def aVeryBigSum(n, ar):
    # Complete this function


def diagonalDifference(a):
    result0 = 0
    result1 = 0
    for i in range(len(a)):
        result0 += a[i][i]
    for i, e in enumerate(reversed(range(len(a)))):
        result1 += a[e][i]
    return abs(result0 - result1)


print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


for i, e in enumerate(reversed(range(len([1, 2, 3])))):
    print(x, y)


def plusMinus(arr):
    value0 = len([*filter(lambda x: x > 0, arr)]) / len(arr)
    value1 = len([*filter(lambda x: x < 0, arr)]) / len(arr)
    value2 = len([*filter(lambda x: x == 0, arr)]) / len(arr)
    return round(value0, 6), round(value1, 6), round(value2, 6)


arr0 = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr0))


print("**".rjust(9))


def staircase(n):
    for i in range(1, n + 1):
        # result += (''.join((i * '#').rjust(n))) + '\n'
        print((i * '#').rjust(n, ' '))


print(staircase(6))


def miniMaxSum(arr):
    from itertools import combinations as cb
    comb = cb(arr, 4)
    result = [sum(i) for i in comb]
    minNum = min(result)
    maxNum = max(result)
    print(minNum, maxNum)


def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))


print(birthdayCakeCandles(4, [3, 2, 1, 3]))


class Test:
    def assert_equal(a, b):
        print(a == b)


def timeConversion(s):
    if s[8:] == "PM":
        if s[:2] == "12":
            return s[:8]
        else:
            firstVal = str((12 + int(s[:2])) % 24).zfill(2)
            result = "{}{}".format(firstVal, s[2:8])
            # print(result)
            return result
    if s[8:] == "AM":
        if s[:2] == "12":
            firstVal = str(int(s[:2]) - 12).zfill(2)
            result = "{}{}".format(firstVal, s[2:8])
            # print(result)
            return result
        else:
            return s[:8]


Test.assert_equal(timeConversion("12:40:22AM"), "00:40:22")
Test.assert_equal(timeConversion("06:40:03AM"), "06:40:03")
Test.assert_equal(timeConversion("12:45:54PM"), "12:45:54")


import primefac
(primefac.primefac(9))


import itertools
result = itertools.chain('ABC3', 'DEF2')
print(*result)
a = itertools.count(3, 2)
print(a)

import itertools


def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


print(*prime_factors(99))


def kFactorization(n, A):
    from itertools import combinations as cb
    from itertools import permutations as pm
    from functools import reduce
    counter = 1
    while counter < len(A) + 1:
        for i in pm(A, counter):
            times_val = reduce(lambda a, b: a * b, i)
            if times_val == n:
                result = [1]
                for x in range(len(i)):
                    result.append(result[x] * i[x])
                return result
        counter += 1
    return [-1]


# arr0 = [2, 3, 4]
# kFactorization(12, arr0)

# arr0 = [2, 10, 6, 9, 11]
# print(kFactorization(15, arr0))

arr0 = [2, 3, 5, 7, 11, 13, 17, 19]
print(kFactorization(231000000, arr0))


def solution(N):
    return " ".join(N.split(" ")[::-1])


arr = [1, 2, 3]
arr = [*map(lambda x:str(x), arr)]
print(' '.join(arr[::-1]))


matrix = [[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]]


def solver(L):
    answer = []
    for x in range(2, len(L)):
        for y in range(2, len(L)):
            hourglasses_array = [
                L[x - 2][y - 2], L[x - 2][y - 1], L[x - 2][y],
                L[x - 1][y - 1],
                L[x][y - 2], L[x][y - 1], L[x][y]
            ]
            answer.append(sum(hourglasses_array))
    return max(answer)


print(solver(matrix))


def solution(N, L):
    for i in range(len(N)):
        print(i)


a0 = [1, 20]
a1 = [120, 130]

solution(a0)


for i in range(2):
    print(i)


print(float(3 / 9))
print(float(3 / 9))

a = input()


s = 'HackerRank '
c = 'is the best place to learn and practice coding!'
print(s + c)

print(*map(lambda x: type(x), [*map(str, [1, 2, 3, 4])]))
[1, 2, 3, 4, 5]
[...]


def solve(grades):
    result = []
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i += 5 - i % 5

        result.append(i)
    return result


arr = [73, 67, 38, 33]

print(solve(arr))


range(32)

print("            73  ".strip())
