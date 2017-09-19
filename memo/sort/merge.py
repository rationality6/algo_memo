import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


def bubble_sort(ARR):
    ARR0 = ARR[:]
    for i in reversed(range(len(ARR0))):
        for z in range(i):
            if ARR0[z] > ARR0[z + 1]:
                ARR0[z], ARR0[z + 1] = ARR0[z + 1], ARR0[z]
    return ARR0


def selection_sort(ARR):
    clone_arr = ARR[:]
    arr_length = len(clone_arr)
    for i in range(arr_length - 1):
        index = i
        for z in range(i + 1, arr_length):
            if clone_arr[index] > clone_arr[z]:
                index = z
        clone_arr[i], clone_arr[index] = clone_arr[index], clone_arr[i]
    return clone_arr


def insertion_sort(ARR):
    clone_arr = ARR[:]
    for i in range(1, len(clone_arr)):
        current = clone_arr[i]
        position = i
        while position > 0 and clone_arr[position - 1] > current:
            clone_arr[position] = clone_arr[position - 1]
            position -= 1
        clone_arr[position] = current
    return clone_arr


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


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


if __name__ == '__main__':
    random_arr0 = random_arr(0, 10)
    print(random_arr0)
    # print(bubble_sort(random_arr0))
    # print(selection_sort(random_arr0))
    print(insertion_sort(random_arr0))
    # print(merge_sort(random_arr0))
