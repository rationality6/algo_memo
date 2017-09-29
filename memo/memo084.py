import numpy as np
x = np.matrix('1 2 3; 3 4 3')
print(x)

y = np.array([[1, 2], [3, 4]])
print(y)


x = [[1, 2], [3, 4]]
result = [[c + d for c, d in zip(a, b)]for a, b in zip(x, x)]
print(result)

2054 / 12 / 12
print(54 % 12)
54 / 12 = 4
54 % 12 = 6
6 / 4 = 1
print(13 % 7)


result = ""
def fibo(n):
    global result
    if n == 0:
        result += "0"
        return 0
    elif n == 1:
        result += "1"
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

fibo(0)
fibo(1)
fibo(3)
print(result)
