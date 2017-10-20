arr0 = [*range(9, -1, -1)]


def get_random_arr(e):
    import random
    arr = [*range(e)]
    for i in range(e):
        rand = random.randint(0, e - 1)
        arr[i], arr[rand] = arr[rand], arr[i]
    return arr


def bubble_sort(L):
    clone = L[:]
    for i in reversed(range(1, len(clone))):
        for z in range(i):
            if clone[z] > clone[z + 1]:
                clone[z], clone[z + 1] = clone[z + 1], clone[z]
    return clone


def insertion_sort(L):
    clone = L[:]
    for i in range(len(clone)):
        c = clone[i]
        p = i
        while 0 < p and c < clone[p - 1]:
            clone[p] = clone[p - 1]
            p -= 1
        clone[p] = c
    return clone


def selection_sort(L):
    clone = L[:]
    length_clone = len(clone)

    for i in range(length_clone):
        index = i
        for z in range(i, length_clone):
            if clone[z] < clone[index]:
                index = z
        clone[i], clone[index] = clone[index], clone[i]
    return clone


def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def merge_sort(L):
    if len(L) <= 1:
        return L
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)


def quick_sort(L):
    pass


arr0 = get_random_arr(10)
print(arr0)
# print(bubble_sort(arr0))
# print(insertion_sort(arr0))
# print(selection_sort(arr0))
# print(merge_sort(arr0))
print(quick_sort(arr0))






import math
from functools import reduce
nu = reduce(lambda a,b:a*b,[*range(28,37)])
result = nu/math.factorial(9)
print(result)
print(len([i for i in range(1,101) if i % 3 == 0 or i % 2 == 0]))
print(len([i for i in range(1,101) if i % 3 == 0 or i % 10 == 0]))
print(len([i for i in range(1,101) if i % 9 == 0 or i % 4 == 0]))
print(len([i for i in range(1,101) if i % 3 == 0 or i % 4 == 0]))
print(len([i for i in range(1,101) if i % 5 == 0 or i % 3 == 0]))
print(len([i for i in range(1,101) if i % 5 == 0 or i % 4 == 0]))
print(len([i for i in range(1,101) if i % 5 == 0 or i % 8 == 0]))
print(len([i for i in range(1,101) if i % 2 == 0 or i % 3 == 0]))
print(len([i for i in range(1,101) if i % 10 == 0 or i % 7 == 0]))
import math
print(math.factorial(6))
import math
a = math.factorial(6)
print(a)

from functools import reduce
print(reduce(lambda a,b:a*b,[*range(7,10)]))

import math
r = math.factorial(60)/(math.factorial(56)*math.factorial(4))
print(r)
print(1/r)

import math
r = math.factorial(45)/(math.factorial(39)*math.factorial(6))
print(r)
print(1/r)

from functools import reduce
n = reduce(lambda a,b:a*b,[*range(97,103)])
import math
d = math.factorial(6)
result = n/d
print(result)
