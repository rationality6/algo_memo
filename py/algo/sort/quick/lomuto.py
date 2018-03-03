import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


def partition(alist):
    pivot = alist[0]
    i = 0
    for j in range(len(alist) - 1):
        if alist[j + 1] < pivot:
            alist[j + 1], alist[i + 1] = alist[i + 1], alist[j + 1]
            i += 1
    alist[0], alist[i] = alist[i], alist[0]
    return i


def quicksort(L, S, E):
    if S < E:
        pivot = partition(L)
        first_part = quicksort(alist[:i])
        second_part = quicksort(alist[i + 1:])
        first_part.append(alist[i])
    return first_part + second_part


if __name__ == "__main__":
    random_arr0 = random_arr(1, 11)
    # random_arr0 = random_arr(0, 5)
    # random_arr0 = [2, 1, 4, 5, 3]
    # random_arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print(random_arr0, 'start')
    print(quicksort(random_arr0), 'end')
