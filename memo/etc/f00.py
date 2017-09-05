def swap():
    a0 = "a"
    b0 = "b"
    print(a0)
    print(b0)

    temp = a0
    a0 = b0
    b0 = temp

    print(a0)
    print(b0)


swap()


a0 = 6
b0 = 8
a0 = a0 + b0  # 14
b0 = a0 - b0  # 6
a0 = a0 - b0  # 8
print(a0)
print(b0)


a0 = 6
b0 = 8
a0 = a0 ^ b0
b0 = a0 ^ b0
a0 = a0 ^ b0
print(a0)
print(b0)


a0 = 6
b0 = 8
a0 = a0 & b0
b0 = a0 & b0
a0 = a0 & b0
print(a0)
print(b0)

print(True & False)
print(False & False)
print(False & True)
print(True & True)
print(False & False)

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
print product


from functools import reduce
def average(list):
    return reduce((lambda x, y: x + y),list) / len(list)
print average([1,2,3,4])
