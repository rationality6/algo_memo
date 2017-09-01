def mystery(alist):
    for index in range(1, len(alist)):
        pos = index
        current = alist[index]
        print(pos, 'post')
        print(current, 'current')
        while pos > 0 and alist[pos - 1] > current:
            print("fo")
            alist[pos] = alist[pos - 1]
            post = pos - 1
        alist[pos] = current


# ls0 = [1, 2, 3, 4, 5]
# ls0 = [8, 5, 6, 7]
ls0 = [9, 8, 6, 7]

mystery(ls0)
print(ls0)


# while False:
#     print("foo?")
#
#
# 1 > 0 and alist[1 - 1] > 2:
# True and 1 > 2
# 1 > 0 and 4 > 5:
# True and 4 > 5:
