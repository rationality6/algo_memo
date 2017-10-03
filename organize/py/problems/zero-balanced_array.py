class Test:
    def assert_equals(result, answer):
        print(result == answer)

    def describe(s):
        print(s)


def is_zero_balanced(arr):
    import collections
    c = collections.Counter(arr)
    return bool(arr) and all(c[k] == c[-k] for k in c)

# def is_zero_balanced(arr):
#     from collections import Counter
#     c = Counter(arr)
#     return bool(arr) and all(c[k] == c[-k] for k in c)


Test.describe("Basic tests")
# Test.assert_equals(is_zero_balanced([3]), False)
# Test.assert_equals(is_zero_balanced([-3]), False)
# Test.assert_equals(is_zero_balanced([0, 0, 0, 0, 0, 0]), True)
Test.assert_equals(is_zero_balanced([0, 1, -1]), True)
# Test.assert_equals(is_zero_balanced([]), False)
# Test.assert_equals(is_zero_balanced([3, -2, -1]), False)
# Test.assert_equals(is_zero_balanced([0]), True)
# Test.assert_equals(is_zero_balanced([1, 1, -2]), False)
# Test.assert_equals(is_zero_balanced([-1, 1, -2, 2, -2, -2, -4, 4]), False)
# Test.assert_equals(is_zero_balanced([0, 0, 0, 0, 0]), True)
