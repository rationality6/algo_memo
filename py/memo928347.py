foo = "foo"


def one():
    foo = "bar"
    two()


def two():
    print(foo)


one()
two()
