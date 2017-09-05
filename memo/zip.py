# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y)
# listed = list(zipped)
# print(listed)
# x2, y2 = zip(*zip(x, y))


def sum_matrix(a, b):
    return [[e + f for e, f in zip(c, d)]for c, d in zip(a, b)]


print(sum_matrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


def sum_matrix01(a, b):
    answer = [[] for i in range(len(a))]
    for i in range(len(a)):
        for x in range(len(a[i])):
            answer[i].append(a[i][x] + b[i][x])
    return answer


print(sum_matrix01([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


def sumMatrix(A, B):
    answer = [[A[i][j] + B[i][j]
               for j in range(len(A[0]))] for i in range(len(A))]
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [3, 4]], [[3, 4], [5, 6]]))

a, b = [[1, 2], [3, 4]], [[3, 4], [5, 6]]
print([c + d for c, d in zip(a, b)])
