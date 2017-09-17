import time


def _fib(n):
    if n < 2:
        return n
    else:
        print('foo')
        return _fib(n - 1) + _fib(n - 2)


cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = n if n < 2 else fib(n - 1) + fib(n - 2)
        return cache[n]


start = time.time()
print(fib(4))
print("{:0.5f}".format(time.time() - start))
start = time.time()
print(_fib(4))
print("{:0.5f}".format(time.time() - start))


def memoize(func):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return decorated_function


@memoize
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(10))


def outer(func):
    private = 99

    def inner(name):
        return "{}{}".format(func(name), private)
    return inner


def foo(text):
    return text


foobar = outer(foo)

print(foobar('hyun'))







def _fib(n):
    if n < 2:
        return n
    else:
        print(n)
        return _fib(n - 1) + _fib(n - 2)
print(_fib(5))
