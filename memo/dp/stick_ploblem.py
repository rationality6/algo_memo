stick_prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod(p, n):
    r = [0]
    for j in range(1, n):
        q = -1
        for i in range(1, j):
            q = max(q, p[i] + r[j - i])
        r[j] = q

    return r[n]


print(cut_rod(stick_prices, 2))  # 5
print(cut_rod(stick_prices, 3))  # 8
print(cut_rod(stick_prices, 4))  # 10
print(cut_rod(stick_prices, 7))  # 18
