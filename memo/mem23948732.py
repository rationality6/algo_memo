rod_price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# def cut_rod(length):
#     cache = [0] * (length + 1)
#     for i in range(1, length + 1):
#         q = 0
#         for z in range(1, i + 1):
#             q = max(q, rod_price[z] + cache[i - z])
#         cache[i] = q
#     return cache[length]

def cut_rod(L):
    cache = [0]
    for i in range(1, L + 1):
        q = 0
        for z in range(1, i + 1):
            q = max(q, rod_price[z] + cache[i - z])
        cache.append(q)
    return cache[L]


print(cut_rod(2))
#; // 5
print(cut_rod(3))
# ; // 8
# print(cut_rod(4))
# ; // 10
# print(cut_rod(7))
# ; // 18


# lcs("ABCBDAB", "BDCABA")

def shoot_rate(p,c):
    return p ** c
