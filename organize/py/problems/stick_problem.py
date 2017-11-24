# 일단 막대기부터 잘라봅시다. 하나의 긴 막대기가 있는데 막대기 조각마다 가격이 다릅니다. 막대기를 적절하게 잘라서 가장 가격이 높게 만들어야 합니다.
#
# 길이(i)   0  1  2  3  4   5   6   7   8   9  10
# 가격(Pi)  0  1  5  8  9  10  17  17  20  24  30


stick_prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod(p, n):
    r = [0]
    for j in range(1, n + 1):
        q = 0
        for i in range(1, n + 1):
            q = max(q, p[i] + r[j - i])


def cut_rod(p, n):
    r = [0]
    for j in range(1, n + 1):
        q = 0
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r.insert(j, q)
    # return r
    return r[n]


print(cut_rod(stick_prices, 2))  # 5
print(cut_rod(stick_prices, 3))  # 8
print(cut_rod(stick_prices, 4))  # 10
print(cut_rod(stick_prices, 7))  # 18
print(cut_rod(stick_prices, 9))  # 25
print(cut_rod(stick_prices, 10))  # 30
