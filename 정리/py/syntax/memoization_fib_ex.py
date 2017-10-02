import time

cache = {}
def fib(n):
    if n not in cache.keys():
        cache[n] = _fib(n)
    return cache[n]

def _fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

st = time.time()
for _ in range(990009):
    # _fib(495)
    fib(495)
    print(cache)
print("{}".format(round(time.time() - st, 5)))


def memoize(f):
    CACHE = {}
    def deco_func(*args):
        if args in CACHE:
            return CACHE[args]
        else:
            CACHE[args] = f(*args)
            return CACHE[args]
    return deco_func

@memoize
def f(N):
    return N if N < 2 else f(N-1) + f(N-2)
print(f(10))




def greet(name):
    def get_message():
        return "Hello "

    result = get_message() + name
    return result


print(greet('Hyun'))


def greet(name):
    return "Hello " + name


def call_func(func):
    other_name = "John"
    return func(other_name)


print call_func(greet)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{}</p>".format(func(name))
    return func_wrapper


@p_decorate
def get_text(name):
    return "lorem ipsum, {} dolor sit amet".format(name)


print(get_text("Hyun"))


def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(13))


# ////////////////////////////////////////////////////////
import time

fib_cache = {}

def _fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = n if n < 2 else fib(n - 1) + fib(n - 2)
        return fib_cache[n]


start = time.time()
print(fib(500))
# print(_fib(500))
print("{:0.4f}".format(time.time() - start))
