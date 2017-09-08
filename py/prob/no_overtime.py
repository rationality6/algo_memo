def no_overtime(n, works):

    if n >= sum(works)
        return 0

    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1

    result = map(lambda x: x**2, works)

    return result


print(no_overtime(4, [4, 3, 3]))


arr0 = [4, 3, 2, 3, 3]
# arr0[arr0.index(max(arr0))] -= 1
# result = sum(map(lambda x: x**2, arr0))
result = sum([w ** 2 for w in arr0])
print(result)


def no_overtime01(n, works):
    if n >= sum(works):
        return 0
    for _ in range(n):
        works[works.index(max(works))] -= 1
    result = sum([i * 2 for i in works])
    return result


print(no_overtime01(4, [4, 3, 3]))
