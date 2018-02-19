def solution(v):
    import collections
    answer = []
    for a in zip(*v):
        b = collections.Counter(a)
        for i in b:
            if b[i] == 1:
                answer.append(i)
    return answer


v = [[1, 4], [3, 4], [3, 10]]
v2 = [[1, 1], [2, 2], [1, 2]]

print(solution(v))
print(solution(v2))
