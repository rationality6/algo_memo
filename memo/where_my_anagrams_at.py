class Test:
    def assert_equals(a, b):
        print(a == b)


def anagrams(word, words):
    import itertools
    result = []
    p = [''.join(i) for i in itertools.permutations(word)]
    print(p)
    for i in words:
        if i in p:
            result.append(i)
    print(result, 'result')
    return result


def anagrams(word, words):
    return ([item for item in words if sorted(word) == sorted(item)])


Test.assert_equals(
    anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams(
    'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


print([*all_perms("ABCD")])

import itertools
c = itertools.product([1, 2, 3, 4], repeat=4)
# print([*c])
print(len([*c]))
# 24
print(4 * 3 * 2 * 1)
print(5 * 4 * 3 * 2 * 1)
print(5**5)
print(5 * 5)
print(4**4)
