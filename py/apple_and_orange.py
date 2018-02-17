# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
#     print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_in = 0
    oranges_in = 0
    for i in apples:
        distance = i + a
        if distance >= s and distance <= t:
            apples_in += 1
    for j in oranges:
        distance = j + b
        if distance >= s and distance <= t:
            oranges_in += 1

    for x in [apples_in, oranges_in]:
        print(x)


print(countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]))
