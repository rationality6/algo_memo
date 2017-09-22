def factorial(N):
    if N <= 1:
        return N
    else:
        return N * factorial(N - 1)


def factorial_tail_rec(N, RES):
    if N == 1:
        return RES
    return factorial_tail_rec(N - 1, RES * N)


def factorial_tail(N):
    return factorial_tail_rec(N, 1)


def recurve_adder(N, REC):
    if N == 1:
        return REC
    else:
        return recurve_adder(N - 1, REC + N)


if __name__ == '__main__':
    # print(factorial(5))
    # print(factorial_tail_rec(5, 1))
    # print(factorial_tail(5))

    print(recurve_adder(10, 1))
