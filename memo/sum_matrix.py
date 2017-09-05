def sumMatrix(A, B):
    answer = []

    for a, b in zip(A, B):

        answer.append([c + d for c, d in zip(a, b)])

    return answer


print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

# [c + d for c, d in zip(a, b)] for a, b in zip(A, B)
