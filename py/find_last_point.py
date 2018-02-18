def find_last_point(L):
    from collections import Counter
    answer = []
    for i in zip(*L):
        count0 = Counter(i)
        for j in count0:
            if count0[j] == 1:
                answer.append(j)
    return answer


# a0 = [[1, 1], [2, 2], [1, 2]]
a1 = [[1, 4], [3, 4], [3, 10]]

# print(find_last_point(a0))
print(find_last_point(a1) == [1, 10])
