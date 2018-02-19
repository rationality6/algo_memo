
list0 = [1, 4, 3, 2]


def reverse(L):
    size = len(L) // 2

    for i in range(size):
        L[i], L[(-1 - i)] = L[(-1 - i)], L[i]
    print(L)


print(reverse(list0))
