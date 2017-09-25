import random


def search(LIST, ITEM):
    position = 0
    found = False
    while position < len(LIST) and not found:
        if LIST[position] == ITEM:
            found = True
        position += 1
    return found


def binary_search(LIST, ITEM):
    found = False
    top = len(LIST) - 1
    bottom = 0
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if LIST[middle] == ITEM:
            found = True
        elif ITEM > LIST[middle]:
            bottom = middle + 1
        else:
            top = middle - 1
    return found


def random_arr(a, b):
    arr0 = [*range(a, b)]
    for i in range(len(arr0)):
        rn = random.randint(0, len(arr0) - 1)
        arr0[i], arr0[rn] = arr0[rn], arr0[i]
    return arr0


def bubble_sort(LIST):
    clone = LIST[:]
    for i in reversed(range(len(clone))):
        for z in range(i):
            if clone[z] > clone[z + 1]:
                clone[z], clone[z + 1] = clone[z + 1], clone[z]
    return clone


def insertion_sort(LIST):
    clone = LIST[:]
    for i in range(len(clone)):
        current = clone[i]
        position = i
        while position > 0 and clone[position - 1] > current:
            clone[position] = clone[position - 1]
            position -= 1
        clone[position] = current
    return clone


def selection_sort(LIST):
    clone = LIST[:]
    arr_length = len(clone)
    for i in range(arr_length - 1):
        index = i
        for z in range(i + 1, arr_length):
            if clone[index] > clone[z]:
                index = z
        clone[i], clone[index] = clone[index], clone[i]
    return clone


def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def merge_sort(LIST):
    if len(LIST) == 1:
        return LIST
    middle = len(LIST) // 2
    left = merge_sort(LIST[:middle])
    right = merge_sort(LIST[middle:])
    return merge(left, right)


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


def lomuto(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] < pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    if A[hi] < A[i + 1]:
        A[hi], A[i + 1] = A[i + 1], A[hi]
    return i + 1


def quick_sort(LIST, start, end):
    if start < end:
        pivot = partition_hoare(LIST, start, end)
        print(LIST)
        # pivot = lomuto(LIST, start, end)
        quick_sort(LIST, start, pivot - 1)
        quick_sort(LIST, pivot + 1, end)
    return LIST


def test(random_func, n, anwser_func):
    result = True
    for i in range(n):
        ran0 = random_func(0, i)
        answer0 = anwser_func(ran0, 0, len(ran0) - 1)
        if sorted(ran0) != answer0:
            result = False
    return result


if __name__ == "__main__":
    # arr0 = [*range(0, 80, 7)]
    # print(arr0)
    # arr1 = random_arr(0, 7)
    # arr1 = [15, 20, 10, 25, 5, 10]
    # print(arr1)
    arr0 = [15, 20, 10, 25, 5, 10]

    # print(bubble_sort(arr1))
    # print(merge_sort(arr1))
    # print(insertion_sort(arr1))
    print(quick_sort(arr0, 0, len(arr0) - 1))
    # print(quick_sort(arr1, 0, len(arr1) - 1))
    # print(selection_sort(arr1))

    # print(search(arr0, 56))
    # print(binary_search(arr0, 7))

    # print(test(random_arr, 100, quick_sort))

    # print(1 is 1)
    # print(1 == 1)
    # print([] == [])
    # print([1] == [1])
    # print([1] == [2])
    # print([1] is [1])
    # print([1] is [2])
    # a = []
    # print(a is a)
