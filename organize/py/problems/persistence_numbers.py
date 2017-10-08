class Test:
    def assert_equals(a, b):
        print(a == b)


def persistence(n):
    from functools import reduce
    count = 0
    while n >= 10:
        queue = [int(i) for i in list(str(n))]
        n = reduce(lambda a, b: a * b, queue)
        count += 1
    return count


Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)
