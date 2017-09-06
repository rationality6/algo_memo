# import numpy as np
# import time
# answer = 0
#
#
# def findLargestSquare(board):
#     global answer
#
#
#     a = np.array(board)
#
#     for k in reversed(range(a[0].size + 1)):
#         conv_size = k
#         for i in range(a[0].size - conv_size + 1):
#             num = i
#             for j in range(a[0].size - conv_size + 1):
#                 #print('i:', i, 'j:', j)
#                 print(a[i:i + conv_size, j:j + conv_size])
#                 #print('unique: ',np.unique(a[i:i+ conv_size,j:j+conv_size]).size)
#                 if(np.unique(a[i:i+ conv_size,j:j+conv_size]).size == 1):
#                     #print("returning")
#                     return len(a[i:i+ conv_size,j:j+conv_size])**2
#                 num = num + 1
#                 print("================")
#     return len(a[i:i+ conv_size,j:j+conv_size])**2

import itertools
import numpy as np


def findLargestSquare(board):
    a = np.array(board)
    max_size = min(a.shape)
    for size in reversed(range(2,  max_size + 1)):
        k = max_size - size + 1
        for i, j in itertools.product(range(k), repeat=2):
            print('checking position: ', (i, j))
            sub_square = a[i:i + size, j:j + size]
            count = len(np.unique(sub_square))
            print(count, ' elements in: \n', sub_square)
            if count == 1:
                return len(sub_square) ** 2
                # if you also want to know the position, you could do
                # return len(sub_square) ** 2 ,  (i, j)
    return 1  # no squares found


testBoard = [
    ['X', 'O', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'X', 'X', 'X']
]

findLargestSquare(testBoard)


import itertools
for a, b in itertools.product(range(3), repeat=3):
    print(a)
    print(b)
