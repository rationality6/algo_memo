def func_0(x):
    return x**2 - 1


def func_1(x):
    return (x + 3)**2 + 5


def func_2(x):
    return -((x**2) / 4) + 7


def func_3(x):
    return (x**2) - 1

# average rate of change


def ARC(func0, x, y):
    a = func0(x)
    b = func0(y)
    print(a, b)
    return (b - a) / (y - x)


# print(ARC(func_0, -1, -3))
# print(ARC(func_1, -4, -3))
# print(ARC(func_2, -2, 4))
# print(ARC(func_2, -2, 4))
print(ARC(func_3, -3, 1))

# import matplotlib.pyplot as plt
# ran0 = [*range(-5, 6)]
# result = [*map(lambda x:func_0(x), ran0)]
# plt.plot(result)
# plt.show()


def func_2(x):
    return -((x**2) / 4) + 7


import matplotlib.pyplot as plt
ran0 = [*range(-10, 11)]
result = [*map(lambda x:func_2(x), ran0)]
plt.plot(result)
plt.show()

print(8 * -8 + 2)

x = 3.5
print(2 * x - 7)


arr0 = [*range(10, 0, -1)]
def selection_sort(L):
    clone = L[:]
    length_clone = len(clone)
    for i in range(length_clone):
        index = i
        for z in reversed(range(i, length_clone)):
            if clone[z] < clone[index]:
                index = z
        clone[i], clone[index] = clone[index], clone[i]
    return clone
print(arr0)
print(selection_sort(arr0))
