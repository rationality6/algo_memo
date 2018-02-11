class Test:
    def assert_equals(a, b):
        print(a)
        print(b)
        pass


def gen_primes(N):
    primes = set()
    for i in range(2, N):
        if all(i % p > 0 for p in primes):
            primes.add(i)
            # yield i
    return primes


print(gen_primes(30))


def consec_kprimes(k, arr):
    pass


def testing(actual, expected):
    Test.assert_equals(actual, expected)


testing(consec_kprimes(3, [10158, 10182, 10184, 10172, 10179,
                           10168, 10156, 10165, 10155, 10161, 10178, 10170]), 5)
# testing(consec_kprimes(2, [10110, 10102, 10097, 10113, 10123,
#                            10109, 10118, 10119, 10117, 10115, 10101, 10121, 10122]), 7)
# testing(consec_kprimes(2, [10123, 10122, 10132, 10129,
#                            10145, 10148, 10147, 10135, 10146, 10134]), 2)
# testing(consec_kprimes(6, [10176, 10164]), 0)
# testing(consec_kprimes(1, [10182, 10191, 10163, 10172, 10178,
#                            10190, 10177, 10186, 10169, 10161, 10165, 10181]), 0)


import matplotlib.pyplot as plt
list0 = [*map(lambda x:x**2, [*range(-10, 11)])]
plt.plot(list0)
plt.show()


def get_components_from_mag(p_mag, p_deg):
    import math
    x = p_mag * math.sin(p_deg)
    y = p_mag * math.cos(p_deg)
    print(math.round(x, 2), y)


get_components_from_mag(12, 20)
