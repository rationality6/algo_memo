def fibonacci_bottom_top(n, a=0, b=1):
    arr = []
    while len(arr) < n:
        a, b = b, a + b
        arr.append(a)
    return arr
print(fibonacci_bottom_top(10))


cache = {}
def fibonacci_memoize(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = n if n < 2 else fibonacci_memoize(
            n - 1) + fibonacci_memoize(n - 2)
        return cache[n]
print(fibonacci_memoize(10))
print(fibonacci_memoize(400))
print(cache)


cache = {}


def fibonacci_memoize(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = n if n < 2 else fibonacci_memoize(
            n - 1) + fibonacci_memoize(n - 2)
        return cache[n]


print(fibonacci_memoize(10))
print(fibonacci_memoize(4000000))
print(cache)
