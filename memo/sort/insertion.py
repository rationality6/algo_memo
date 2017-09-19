import random


def random_array_maker(N):
    arr0 = [*range(N)]
    for i in range(N):
        ran0 = random.randint(0, N - 1)
        arr0[i], arr0[ran0] = arr0[ran0], arr0[i]
    return arr0


def insertion_sort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        position = i
        while 0 < position and current < alist[position - 1]:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = current


def bubble(alist):
    for i in reversed(range(len(alist))):
        for z in range(i):
            if alist[z] > alist[z + 1]:
                alist[z], alist[z + 1] = alist[z + 1], alist[z]


def selection_sort(ARR):
    arr_length = len(ARR)
    for i in range(arr_length - 1):
        index = i
        for z in range(i + 1, arr_length):
            if ARR[index] > ARR[z]:
                index = z
        ARR[index], ARR[i] = ARR[i], ARR[index]


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(ARR):
    if len(ARR) <= 1:
        return ARR
    middle = len(ARR) // 2
    left = merge_sort(ARR[:middle])
    right = merge_sort(ARR[middle:])
    return merge(left, right)


if __name__ == '__main__':
    list0 = random_array_maker(20)
    print(list0)
    # insertion_sort(list0)
    # bubble(list0)
    # selection_sort(list0)
    print(merge_sort(list0))
