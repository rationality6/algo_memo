def solution(n):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(0, n)))


print(solution(1000))
