# import hashlib
#
# a = hashlib.sha256("foobar").hexdigest()
# print(a)

x = -15

if x == 0:
    print(x, "is zero")
elif x > 0:
    print(x, "is positive")
else:
    print(x, "d")

for i in [2, 3, 5, 7]:
    print(i)

i = 0

while i < 0:
    print(i, end=' ')
    i += 1

for i in range(20):
    if i % 2 == 0:
        continue
    print(i, end=' ')

a, b = 0, 1
amax = 100
l = []

while True:
    (a, b) = (b, a + b)
    if a > amax:
        break
    l.append(a)
print(l)


a, b = 0, 1
l = []

while True:
    a, b = b, a + b
    if a > 100:
        break
    l.append(a)
print(l)
