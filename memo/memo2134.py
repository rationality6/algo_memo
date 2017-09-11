import collections


def solution(v):
    answer = []
    for i in zip(*v):
        y = collections.Counter(i)
        for z in y:
            if y[z] == 1:
                answer.extend([z])
    print(answer)
    return answer

# ////////////////////////////////


import collections


def solution(v):
    answer = []

    for i in zip(*v):
        c = collections.Counter(i)
        for z in c:
            if c[z] == 1:
                answer.append(z)
    # for i in c:
    # print(i)

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
# [1, 10]
print(solution([[1, 1], [2, 2], [1, 2]]))
# [2, 1]
