import numpy as np
import math
import lib

a0 = np.array(lib.get_components_from_mag(12, 20))
a1 = np.array([0, 8])
a0 = a0 * np.array([-1, 1])
a2 = a0 - a1

# print(lib.get_mag_from_components(12,5)-lib.get_mag_from_components(13,-8))


import numpy as np
a = np.array([12, 5])
b = np.array([13, -8])
c = b - a
# print(c)
# print(lib.get_mag_from_components(c[0],c[1]))
# print(2,lib.get_mag_from_components(c[0],c[1]))

# print(lib.get_mag_from_components(12,5))

result = math.sqrt((a2[0] ** 2) + (a2[1]**2))
result = lib.get_mag_from_components(a2[0], a2[1])
# print(round(result, 2))

# print(math.degrees(math.atan(lib.get_components_from_mag(12, 20)[1]/lib.get_components_from_mag(12, 20)[0]))+90)
# print(((math.degrees(math.atan(a2[0] / a2[1]))) * -1) + 90)

# print(lib.get_mag_from_components(lib.get_mag_from_components(3,4),lib.get_mag_from_components(1,1)))
a = np.array([3, 4])
b = np.array([1, 1])
c = a - b
a = lib.get_mag_from_components(5, 2)
b = lib.get_mag_from_components(-6, 1)
print(lib.get_mag_from_components(1, 3))


def bubble_sort(L):
    return L


print(selection_sort([5, 4, 3, 2, 1]))
