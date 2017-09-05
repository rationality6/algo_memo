import numpy as np


def sumMatrix(A, B):
    return (np.array(A) + np.array(B)).tolist()


print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
