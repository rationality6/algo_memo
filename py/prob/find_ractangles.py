from collections import Counter


def solution(v):
    result = []
    for i in zip(*v):
        count = Counter(i)
        for z in count:
            if count[z] == 1:
                result.extend([z])
    return result


v = [[1, 4], [3, 4], [3, 10]]
v1 = [[1, 1], [2, 2], [1, 2]]

print(solution(v))
print(solution(v1))
