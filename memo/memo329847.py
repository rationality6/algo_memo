def bubble(L):
    clone = L[:]
    for i in reversed(range(len(clone))):
        for z in range(i):
            clone[z], clone[z + 1] = clone[z + 1], clone[z]
    return clone


arr0 = [*reversed(range(0, 10))]
print(arr0)
print(bubble(arr0))
