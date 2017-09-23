import random


def random_arr(a, b):
    arr0 = [*range(a, b)]
    for i in range(len(arr0)):
        rn = random.randint(0, len(arr0) - 1)
        arr0[i], arr0[rn] = arr0[rn], arr0[i]
    return arr0


def q_sort(lists, low, high):
    if low >= high:
        return
    ip = low
    ib = ip + 1
    for i in range(ip + 1, high + 1):
        if lists[i] < lists[ip]:
            if i != ib:
                lists[i], lists[ib] = lists[ib], lists[i]
            ib += 1
    lists[ip], lists[ib - 1] = lists[ib - 1], lists[ip]
    print(lists)
    # q_sort(lists, low, ib - 2)
    # q_sort(lists, ib, high)
    return lists


def partition_hoare(LIST, start, end):
    pivot = LIST[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and LIST[left] <= pivot:
            left += 1
        while left <= right and pivot <= LIST[right]:
            right -= 1
        if right < left:
            done = True
        else:
            LIST[left], LIST[right] = LIST[right], LIST[left]
    LIST[start], LIST[right] = LIST[right], LIST[start]
    return right


def quick_sort(LIST, start, end):
    if start < end:
        pivot = partition_hoare(LIST, start, end)
        print(LIST)
        quick_sort(LIST, start, pivot - 1)
        quick_sort(LIST, pivot + 1, end)
    return LIST

def binary_search(LIST):
    pass

if __name__ == '__main__':
    arr0 = random_arr(0, 10)
    # print(arr0)
    arr0 = [1, 7, 2, 8, 9, 6, 5, 3, 4, 0]
    # arr0 = [15, 20, 10, 25, 5, 10]
    # print(q_sort(arr0, 0, len(arr0) - 1))
    print(quick_sort(arr0, 0, len(arr0) - 1))
