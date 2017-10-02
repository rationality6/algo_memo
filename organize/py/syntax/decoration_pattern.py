def decoratorExample(func):
    def wrapFunc(*args, **kargs):
        print("Start", func.__name__)

        func(*args, **kargs)

        print("End", func.__name__)
    return wrapFunc


@decoratorExample
def test(a, b, c):
    print("Variables :", a, b, c)


test("1", 2, c="345")
