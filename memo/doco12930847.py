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
