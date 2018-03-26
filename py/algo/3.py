# 3. 숫자 배열 순서 바꾸기
# 입력된 숫자 배열을 다음과 같은 형태의 배열로 순서를 변경하라.
# [a1, a2, a3..., an, b1, b2, b3..., bn]
# =>
# [a1, b1, a2, b2, a3, b3..., an, bn]
# 예)
# 입력 : 1 4 5 2 4 8
# 출력 : 1 2 4 4 5 8


list0 = [1, 4, 5, 2, 4, 8]
answer = [1, 2, 4, 4, 5, 8]


def solution(L):
    middle = len(L) // 2
    left = L[:middle]
    right = L[middle:]
    result = []
    for i in zip(left, right):
        result.extend(i)
    # print(left)
    # print(right)
    return result


print(solution(list0))
