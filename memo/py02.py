import collections

v = [[1, 4], [3, 4], [3, 10]]
v2 = [[1, 1], [2, 2], [1, 2]]

for i in zip(*v):
    y = collections.Counter(i)
    print(y)
