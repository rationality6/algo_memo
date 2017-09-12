from random import randint


def random_alist(n):
    arr0 = [i for i in range(n)]

    for i in range(0, len(arr0)):
        random_number = randint(0, len(arr0) - 1)
        temp = arr0[i]
        arr0[i] = arr0[random_number]
        arr0[random_number] = temp
    return arr0


arr0 = random_alist(10)
print(arr0)


def insertion(alist):
    for i in range(1, len(alist)):
        cur = alist[i]
        pos = i
        while 0 < pos and cur < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = cur


insertion(arr0)
print(arr0)


# //////////////////////////////

from random import randint


def random_alist(n):
    arr0 = [i for i in range(n)]

    for i in range(0, len(arr0)):
        random_number = randint(0, len(arr0) - 1)
        temp = arr0[i]
        arr0[i] = arr0[random_number]
        arr0[random_number] = temp

    return arr0


def bubble(alist):
    for i in reversed(range(len(alist))):
        for z in range(i):
            if alist[z] > alist[z + 1]:
                alist[z], alist[z + 1] = alist[z + 1], alist[z]


a = random_alist(10)
print(a)
bubble(a)
print(a)
