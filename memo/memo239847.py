arr0 = [23, 29, 20, 32, 23, 21, 33, 25]


def sort(LL):
    L = LL[:]
    for i in reversed(range(len(L))):
        for y in range(i):
            if L[y] > L[y + 1]:
                L[y], L[y + 1] = L[y + 1], L[y]
    return L


print(sort(arr0))


print(sum(sort(arr0)) / len(arr0))

# mean 25.75
# median:24
# mode:23

def

arr1 = [9, 10, 6, 5, 6]
print(sum(arr1) / len(arr1))

arr2 = [10, 6, 4, 4, 6, 4, 1]
print(sum(arr2) / len(arr2))


L = [6, 4, 1, 9, 3, 8, 3, 5, 10]
for i in reversed(range(len(L))):
    for y in range(i):
        if L[y] > L[y + 1]:
            L[y], L[y + 1] = L[y + 1], L[y]
print(L)


print((273 * 5) - (244 + 353 + 235 + 311))

print(sum([4, 5, 5, 6, 8, 8]) / 6)

import numpy as np
arr0 = [1,2,3,4,5,6]
print(np.mean(arr0))
