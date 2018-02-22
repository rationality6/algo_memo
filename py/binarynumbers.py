
# import sys
#
#
# n = int(input().strip())

n0 = 5
n1 = 13
n2 = 439


class Test:
    def assult_equals(a, b):
        print(a == b)

    def assult_equal0(a, b):
        print('works')


def solution(N):
    # from functools import map
    max_count = 0
    maximum = 0
    array = list(bin(N)[2:])
    array_int = [*map(lambda x: int(x), array)]
    print(array_int)
    for i in range(1, len(array_int)):
        if(array_int[i] == array_int[i - 1]):
            max_count += 1
        else:
            maximum = max(maximum, max_count)
            max_count = 0
    return max(maximum, max_count) + 1


Test.assult_equals(solution(n0), 1)
Test.assult_equals(solution(n1), 2)
Test.assult_equals(solution(n2), 3)



from itertools import groupby
data0 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
print(data0)

def len_iter(items):
    return sum(1 for _ in items)

def consecutive_one(data):
    for val, run in groupby(data):
        sum(for i in run)
            sum(1)
print(consecutive_one(data0))
