# import hashlib
# print(hashlib.sha256("oxford").hexdigest())


def fibonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L


print(fibonacci(10))


def fibonacci_recersive(N):
    if N < 2:
        return N
    else:
        return fibonacci_recersive(N - 1) + fibonacci_recersive(N - 2)


print(fibonacci_recersive(10))


def catch_all(*args, **kwargs):
    print("args = ", args)
    print("kwargs ", kwargs)


catch_all(1, 2, 3, a=4, b=5)

catch_all('a', keyword=2)

import numpy as np

a = np.array([[3, 2], [3, 2]])
b = np.array([[3, 2], [3, 2]])
c = a * b
print(c)


def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(1, 2, 3, 4)


def add(x, y): return x + y


print(add(1, 2))


data = [
    {'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
    {'first': 'Grace', 'last': 'Hopper',     'YOB': 1906},
    {'first': 'Alan',  'last': 'Turing',     'YOB': 1912},
]

a = sorted(data, key=lambda item: item['YOB'])
print(a)

print(2 / 0)

try:
    print("let's try something:")
    x = 1 / 0
except:
    print("something bad happeded")

raise ValueError("d")


def fibonacci(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    result = []
    a, b = 0, 1
    while len(result) < N:
        a, b = b, a + b
        result.append(a)
    return result


N = 10

try:
    print("trying this...")
    print(fibonacci(N))
except:
    print("Bad value: need to do something else")


class A:
    def stackoverflow(self, i='default'):
        if i == 'default':
            print("only method")
        else:
            print("got the value")


ob = A()
ob.stackoverflow(2)
ob.stackoverflow()


class Parent():
    def __init__(self):
        pass

    def Create(self):
        return 'Password'


class Child():
    def __init__(self):
        self.Create()

    def Create(self):
        pass
        # return 'The ' + super(Child, self).Create()


print Child().Create()


class MySpecialError(ValueError):
    pass


raise MySpecialError("foo")

try:
    x = 1 / 0
except MySpecialError() as err:
    print("Error class is: ", type(err))
    print("Error message is: ", err)


print(range(10))

print(iter(range(10)))


from itertools import count
for i in count():
    # if i >= 10:
    #     break
    print(i)


L = [2, 4, 6, 8, 10]
for i, val in enumerate(L):
    print(i, val)

L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
print([[lval, rval] for lval, rval in zip(L, R)])

for val in map(lambda x: x ** 2, range(10)):
    print(val, end=' ')

for val in filter(lambda x: x % 2 == 0, range(10)):
    print(val, end=' ')


print([i for i in map(lambda x: x * x, range(10))])
print([i for i in filter(lambda x: x > 5, range(10))])

print([*range(3, 10)])

print([*map(lambda x: x ** 2, range(10))])

print([*filter(lambda x: x % 2 == 0, range(0, 10 + 1))])

l1 = (1, 2, 3, 4)
l2 = ('a', 'b', 'c', 'd')
z = zip(l1, l2)
print(z)
new_L1, new_L2 = zip(*z)
print(new_L1, new_L2)


l1 = [1, 2, 3]
l2 = [1, 2, 3, 4]
z = zip(l1, l2)
a, b = zip(*z)
print(a, b)

l = [*filter(lambda x:x % 2 == 0, range(1, 11))]
r = [*map(lambda x:x * 3, range(1, 6))]
for lval, rval in zip(l, r):
    print(lval, rval)

from itertools import permutations
p = permutations(range(3))
print(*p)
