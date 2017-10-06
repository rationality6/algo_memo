
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


my_get_text = p_decorate(get_text)

print(my_get_text("John"))


def get_text(name):
    return "lorem ipsum, {} dolor sit amet".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return '<p>{}</p>'.format(func(name))
    return func_wrapper


my_get_text = p_decorate(get_text)

print(my_get_text('Hyun'))


class test:
    def assert_equals(a, b):
        print(a == b)

from functools import lru_cache

@lru_cache(None)
def fibonacci(N):
    if N in [0,1]:
        return N
    return fibonacci(N-1) + fibonacci(N-2)

test.assert_equals(fibonacci(70), 190392490709135)
test.assert_equals(fibonacci(60), 1548008755920)
test.assert_equals(fibonacci(50), 12586269025)
