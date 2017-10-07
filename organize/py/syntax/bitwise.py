# 0000 1010
x = 10
# 0000 0100
y = 4

# bitwise and
print("x & y", x & y)
# bitwise or
print("x | y", x | y)
# bitwise inversion -(x+1)
print(~x)
print(~y)

# 0000 0001
x = 1
# 0000 0011
y = 3

# xor
print(x ^ y)

# 0000 1010
x = 10
print(x >> 1)
print(x >> 2)

# 0000 0011
# 0001 1000
print(3 << 3)

# 1000 0000
# 0010 0000 0000
print(128 << 2)
