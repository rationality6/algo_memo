import math
arr0 = [-10, 0, 10, 20, 30]
arr1 = [8, 9, 10, 11, 12]


def get_variance(L):
    leng = len(L)
    mean = sum(L) / leng
    result = []

    for i in range(leng):
        result.append((L[i] - 10)**2)

    variance = sum(result) / leng
    return variance

# print(get_variance(arr0))
# print(get_variance(arr1))


kansas = [23, 25, 28, 28, 32, 33, 35]
paradise = [16, 24, 26, 26, 26, 27, 28]

print(get_variance(kansas))
print(get_variance(paradise))

import math
a = math.sqrt(3.5)
print(a)
import math
a = math.sqrt(5.2)
print(a)


# data0 = [31, 33, 36, 41, 34]
# data1 = [6, 5, 13, 8]
# data2 = [18,16,15,15,16]
# data3 = [4,21,11,6,8]
# data4 = [21,24,24,27,29]
# data5 = [5,6,5,10,9]
# data6 = [41,46,52,49]
data7 = [4, 11, 6, 7]


def get_standard_diviation(L):
    import math
    leng = len(L)
    mean = sum(L) / leng
    sig = 0.0
    for i in L:
        sig += (i - mean)**2
    return math.sqrt(sig / leng)


# print(get_standard_diviation(data0))
# print(get_standard_diviation(data1))
# print(get_standard_diviation(data2))
# print(get_standard_diviation(data3))
# print(get_standard_diviation(data4))
# print(get_standard_diviation(data5))
# print(get_standard_diviation(data6))
print(get_standard_diviation(data7))

arr0 = [3, 15, 21, 13]
arr0 = [5, 9, 5, 5, 7, 11]
arr0 = [1.5, 0, 4, 2.5]
arr0 = [7, 2, 4, 3]
arr0 = [2, 1, 2, 0, 2, 4, 3]

arr0 = [26, 31, 39, 32]


def get_mad(L):
    import math
    leng = len(L)
    mean = sum(L) / leng
    result = []
    for i in range(leng):
        result.append(abs(L[i] - mean))
    print(result)
    print(sum(result))
    print(leng)
    return float(sum(result)) / leng


print(get_mad(arr0))

a = [16, 16, 16, 16, 21, 23, 23, 25, 26, 26, 28, 28]
print(sum(a) / 12)
a = [16, 16, 16, 20, 21, 21, 23, 25, 26, 26, 28, 28]
print(sum(a) / 12)
