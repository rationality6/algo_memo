# 1차시도
def solution(n, arr1, arr2):
    answer = []

    first_binary_arr = []
    second_binary_arr = []
    final_binary_arr = []

    for i in arr1:
        first_binary_arr.append(bin(i)[2:].zfill(n))
    for i in arr2:
        second_binary_arr.append(bin(i)[2:].zfill(n))

    for a, b in zip(first_binary_arr, second_binary_arr):
        for c, d in zip(list(a), list(b)):
            if int(c) == 0 and int(d) == 0:
                final_binary_arr.append(' ')
            else:
                final_binary_arr.append('#')

    final_binary_arr = ''.join(final_binary_arr)

    for i in range(0, n * n, n):
        answer.append(final_binary_arr[i:i + n])

    return answer


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(5, arr1, arr2))

# arr1 = [46, 33, 33 ,22, 31, 50]
# arr2 = [27 ,56, 19, 14, 14, 10]
# print(solution(6, arr1, arr2))

# 2차시도


def solution(n, arr1, arr2):
    answer = []
    result = []
    for i in [bin(a | b)[2:].zfill(n) for a, b in zip(arr1, arr2)]:
        for z in list(i):
            answer.append(' 'if int(z) == 0 else '#')
    answer = ''.join(answer)
    for i in range(0, n * n, n):
        result.append(answer[i:i + n])
    return result


# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# print(solution(5, arr1, arr2))

arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(6, arr1, arr2))


# 3차
def solution(n, arr1, arr2):
    return [format((a | b), '0{}b'.format(n)).replace('0', ' ').replace('1', '#') for a, b in zip(arr1, arr2)]


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(5, arr1, arr2))


arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(6, arr1, arr2))


print(format((46 | 27), 'b'))
