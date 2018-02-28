class Test:
    def assert_equal(A, B):
        pass

    def it():
        print("Here")


Test.it()


def fibo_recor(N):
    if 2 > N:
        return 1
    else:
        return fibo_recor(N - 1) + fibo_recor(N - 2)


print(fibo_recor(5))


def fibo_recor(N):
    if 2 < N:
        return 1
    else:
        return fibo_recor(N - 1) + fibo_recor(N - 2)


print(fibo_recor(5))


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
