import functools


def no_over_time(n, works):
    result = 0

    total_works = functools.reduce((lambda a, b: a + b), works)
    if n >= total_works:
        return
    for i in range(n):
        works[works.index(max(works))] -= 1

    result = sum(map((lambda a: a ** 2), works))

    return result


print(no_over_time(4, [4, 3, 3]))


def noOvertime(n, works):
    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1

    return sum(num * num for num in works)


print(noOvertime(4, [4, 3, 3]))
