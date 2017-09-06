import numpy as np

m0 = [[1, 2, 3, 3], [3, 4, 5, 6]]
m1 = [[1, 2, 3, 4], [3, 4, 5, 6]]
print(np.array(m0))
print(np.unique(m0))


result = 0
for i in list(str(382)):
    result += int(i)
print(result)


arr = [1, 2, 3, 4]


# def foo(arr):
#     try:
#         for i in range(1, len(arr) + 1):
#             print(arr.index(i))
#         return True
#     except Exception as e:
#         return False
#
#
# print(foo(arr))


def solution(arr):
    answer = True

    a = [i for i in range(1, len(arr) + 1)]
    if a != sorted(arr):
        answer = False
    return answer
