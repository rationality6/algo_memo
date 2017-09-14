import random


def random_array_maker(N):
    arr0 = [*range(N)]
    for i in range(N):
        ran0 = random.randint(0, N - 1)
        arr0[i], arr0[ran0] = arr0[ran0], arr0[i]
    return arr0


def insertion_sort(alist):
    for i in range(1, len(alist)):
        cur = alist[i]
        pos = i
        while 0 < pos and cur < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = cur


def bubble(alist):
    for i in reversed(range(len(alist))):
        for z in range(i):
            if alist[z] > alist[z + 1]:
                alist[z], alist[z + 1] = alist[z + 1], alist[z]


list0 = random_array_maker(20)
print(list0)
# insertion_sort(list0)
bubble(list0)
print(list0)
