import time
st = time.time()

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


for _ in range(990000):
    # _fib(495)
    fib(495)


print("{}".format(round(time.time() - st, 2)))


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function


@memoize
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


print(fib(15))


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
