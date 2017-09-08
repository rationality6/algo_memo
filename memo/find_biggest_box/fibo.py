def fibo(n):
    if n < 2:
        # print(n)
        return n
    else:
        # print(n)
        return fibo(n - 1) + fibo(n - 2)


# print(fibo(10))
print(fibo(94))
