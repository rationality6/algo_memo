result = []


def solution(n):
    if n < 2:
        return n
    else:
        # result.append(solution(n - 2) + solution(n - 1))
        # return result
        return solution(n - 2) + solution(n - 1)


print(solution(10))


def fibonacci_bottom_top(n, a=1, b=1):
    arr = []
    while len(arr) < n:
        a, b = b, a + b
        arr.append(a)
    return arr


print(fibonacci_bottom_top(4000000))


cache = {}


def fiba(n):
    cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fiba(n - 1) + fiba(n - 2))
    return cache[n]


n = 0
x = 0
while fiba(x) <= 4000000:
    if not fiba(x) % 2:
        n = n + fiba(x)
    x = x + 1
print(n)


print([i for i in range(10, 100)])
print(125**5)
