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
