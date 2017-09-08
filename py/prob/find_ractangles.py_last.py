import collections


def solution(v):
    answer = []

    for i in zip(*v):
        y = collections.Counter(i)
        for i in y:
            if y[i] == 1:
                answer.extend([i])
    return answer


v = [[1, 4], [3, 4], [3, 10]]
v2 = [[1, 1], [2, 2], [1, 2]]


print(solution(v))
print(solution(v2))


#
# import numpy as np
#
# arr0 = [1,2,3,4,5]
# print(arr0)
# ndarr = np.array(arr0)
# print(ndarr)

#
# x = [1,2,3]
# x.append([4,5])
# print(x)
#
# x = [1,2,3]
# x.extend([4,5])
# print(x)

import collections

x = [1, 2, 3, 5, 6, 7, 5, 2]
print(x)
y = collections.Counter(x)
print(y)

for i in zip(*[[1, 4], [3, 4], [3, 10]]):
    print(i)
