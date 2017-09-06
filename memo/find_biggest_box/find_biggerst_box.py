import numpy as np


def findLargestSquare(board):
    answer = 0

    nd = np.array(board)
    print(nd.shape)

    return answer


testBoard = [
    ['X', 'O', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'X', 'X', 'X']
]

print(findLargestSquare(testBoard))


import numpy as np
import time
answer = 0


def findLargestSquare(board):
    global answer

    a = np.array(board)

    for k in reversed(range(a[0].size + 1)):
        conv_size = k
        for i in range(a[0].size - conv_size + 1):
            num = i
            for j in range(a[0].size - conv_size + 1):
                #print('i:', i, 'j:', j)
                print(a[i:i + conv_size, j:j + conv_size])
                #print('unique: ',np.unique(a[i:i+ conv_size,j:j+conv_size]).size)
                if(np.unique(a[i:i + conv_size, j:j + conv_size]).size == 1):
                    # print("returning")
                    return len(a[i:i + conv_size, j:j + conv_size])**2
                num = num + 1
                print("================")
    return len(a[i:i + conv_size, j:j + conv_size])**2


# testBoard = [['x','o','g'],['b','a','j'],['u','q','p']]


testBoard = [
    ['X', 'O', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'X', 'X', 'X']
]


print(findLargestSquare(testBoard))

print(5 ^ 6)
