# import numpy as np
# list0 = [2, 1, -5]
# list1 = [1, 3, 1]
# npa0 = np.array(list0)
# npa1 = np.array(list1)
# print(npa0 * npa1)


import random
import collections

bottle0 = [0 if i > 50 else 1 for i in range(1, 101)]
b = collections.Counter(bottle0)

for i in range(len(bottle0)):
    rn = random.randint(0, len(bottle0) - 1)
    bottle0[i], bottle0[rn] = bottle0[rn], bottle0[i]


def pick(B, C):
    pick = []
    for i in range(C):
        rn = random.randint(0, len(B) - 1)
        pick.append(B[rn])
    cp = collections.Counter(pick)
    return cp


print(pick(bottle0, 10))
print(pick(bottle0, 100000))


import math
print(6 * math.sin(math.radians(50)))
print(5 * math.tan(math.radians(65)))

import math
print(5 / math.cos(math.radians(65)))
print(math.sqrt((5**2) + ((5 * math.tan(math.radians(65)))**2)))
