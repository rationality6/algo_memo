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
