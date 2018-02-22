list0 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


list1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]


# list1[0][0], list1[0][1], list1[0][2]
#     list1[1][1]
# list1[2][0], list1[2][1], list1[2][2]


def solution(L):
    leng = len(L)
    result_count = 0
    result = 0
    for i in range(2, leng):
        for j in range(2, leng):
            result_count = sum(
                [L[i][j], L[i][j - 1], L[i][j - 2],
                 L[i - 1][j - 1],
                 L[i - 2][j], L[i - 2][j - 1], L[i - 2][j - 2]]
            )
            result = max(result_count, result)
    return result


print(solution(list1))
