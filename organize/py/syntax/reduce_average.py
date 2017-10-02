from functools import reduce


def average(list):
    return reduce((lambda x, y: x + y), list) / len(list)


print(average([1, 2, 3, 4]))
