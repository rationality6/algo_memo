class Test:
    def assert_equals(anwser_code, anwser):
        print(anwser_code == anwser)



CACHE = {}
def divisor_cache(N):
    if N not in CACHE:
        CACHE[N] = sum([i * i for i in range(1, N + 1) if N % i == 0])
        return CACHE[N]
    return CACHE[N]

def list_squared(m, n):
    import math
    result = []
    for i in range(m, n):
        sqrted = math.sqrt(divisor_cache(i))
        if sqrted.is_integer():
            b = sqrted**2
            result.append([i, b])
    return result


Test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
Test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
Test.assert_equals(list_squared(250, 500), [[287, 84100]])
