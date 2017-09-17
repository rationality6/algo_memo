def solution(dartResult):
    answer = 0

    list_result = list(dartResult)
    for i in range(len(list_result)):
        if list_result[i] == 'S':
            list_result[i - 1] = int(list_result[i - 1]) * 1
        elif list_result[i] == 'D':
            list_result[i - 1] = int(list_result[i - 1]) * int(list_result[i - 1])

    print(list_result)

    return answer


print(solution("1S2D*3T"))
