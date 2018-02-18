
ex0 = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 0]
]

ex1 = [
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1]
]

ex2 = [
    [0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1]
]


def solution(L):
    answer = 0
    dp = L[:]
    for i in range(1, len(dp)):
        for j in range(1, len(dp)):
            if dp[i][j] != 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    print(dp)
    maximum_val = max(max(dp))
    answer = maximum_val ** 2
    return answer


print(solution(ex0))
print(solution(ex1))
print(solution(ex2))
