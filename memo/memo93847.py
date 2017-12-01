# import numpy as np
# list0 = [2, 1, -5]
# list1 = [1, 3, 1]
# npa0 = np.array(list0)
# npa1 = np.array(list1)
# print(npa0 * npa1)


import random
import collections


def make_suffle_bottle():
    arr0 = [0 if i > 50 else 1 for i in range(1, 101)]
    for i in range(len(arr0)):
        rn = random.randint(0, len(arr0) - 1)
        arr0[i], arr0[rn] = arr0[rn], arr0[i]
    return arr0


def pick(B, C):
    pick = []
    for i in range(C):
        rn = random.randint(0, len(B) - 1)
        pick.append(B[rn])
    cp = collections.Counter(pick)
    return cp

# print(collections.Counter(make_suffle_bottle()))


print(pick(make_suffle_bottle(), 10))
print(pick(make_suffle_bottle(), 100000))


# import math
# print(6 * math.sin(math.radians(50)))
# print(5 * math.tan(math.radians(65)))
#
# import math
# print(5 / math.cos(math.radians(65)))
# print(math.sqrt((5**2) + ((5 * math.tan(math.radians(65)))**2)))
