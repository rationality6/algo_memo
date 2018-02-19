x = [[1, 2], [3, 4]]
result = [[c + d for c, d in zip(a, b)]for a, b in zip(x, x)]
print(result)

import numpy as np
x = np.matrix('1 2 3; 3 4 3')
print(x)

y = np.array([[1, 2], [3, 4]])
print(y)
