import time


def greet(name):
    return "hello" + name


greet_someone = greet
print(greet_someone("Hyun"))


def greet(name):
    def get_message():
        return "Hello "

    result = get_message() + name
    return result


print(greet("John"))

# ////////////////////////////////


def greet(name):
    return "Hello " + name


def call_func(func):
    other_name = "John"
    return func(other_name)


print(call_func(greet))


def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message


greet = compose_greet_func()
print(greet())


def compose_greet_func(name):
    def get_message():
        return "Hello there " + name

    return get_message


greet = compose_greet_func("John")
print(greet())


def get_text(name):
    return "lorem ipsum, {} dolor sit amet".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{}</p>".format(func(name))
    return func_wrapper


my_get_text = p_decorate(get_text)

print(my_get_text("Hyun"))
####################


def div_decorate(func):
    def func_wrapper(text):
        return "<div>{}</div>".format(text)
    return func_wrapper


@div_decorate
def text_func(text):
    return text


print(text_func("Hyun"))

#########################


def div_decorate(func):
    def func_wrapper(text):
        return "<div>{}</div>".format(text)
    return func_wrapper


def text_func(text):
    return text


result_func = div_decorate(text_func)

print(result_func("Hyun"))


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def wrap_func(text):
        return "<div>{}</div>".format(func(text))
    return wrap_func


@p_decorate
@strong_decorate
@div_decorate
def name(name):
    return name


print(name("Hyun"))

#////


def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family


my_person = Person()
print(my_person.get_fullname())


# ////////////////


def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family


my_person = Person()

print my_person.get_fullname(1, 2, 3, 4)


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
@tags("div")
def get_text(name):
    return "Hello " + name


print get_text("John")

# Outputs <p>Hello John</p>


cache = {}


def fib(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            cache[n] = n
        else:
            cache[n] = fib(n - 2) + fib(n - 1)
        # cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return cache[n]
    return cache


print(fib(10))
print(cache)


def memoization_deco(func):
    cache = {}

    def wapper(*n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(*n)
            return cache[n]
    return wapper


@memoization_deco
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


print(fib(10))


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function, cache


@memoize
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


a, b = fib(10)
print(a)


def fib(n):
    __fib_cache = {}
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        # __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)

    return __fib_cache[n]


print(fib(5))

import functools


def solution(n):
    return functools.reduce(lambda a, b: a + b, list(map(int, list(str(n)))))


print(solution(143))

print(list(map(int, list(str(143)))))

# ////////////////////////
