class Test:
    def assert_equals(anwser_code, anwser):
        print(anwser_code == anwser)


import math


def divisor(N):
    result = []
    for i in range(1, N + 1):
        if N % i == 0:
            result.append(i)
    return result


def sum_list_squared(ARR):
    result = 0
    for i in ARR:
        result += (i ** 2)
    return result


def list_squared(m, n):
    result = []
    for i in range(m, n):
        divied = divisor(i)
        sum_list = sum_list_squared(divied)
        squared_result = math.sqrt(sum_list)
        if squared_result.is_integer():
            b = sum_list
            result.append([i, b])
    return result


Test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
Test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
Test.assert_equals(list_squared(250, 500), [[287, 84100]])


print(-(-2**2)**3 / 2)
print(-2**2)
