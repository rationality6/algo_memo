import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


random_arr0 = random_arr(0, 10)
print(random_arr0)


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


def merge_sort(ARR):
    if len(ARR) <= 1:
        return ARR
    middle = int(len(ARR) / 2)
    left = merge_sort(ARR[:middle])
    right = merge_sort(ARR[middle:])
    return merge(left, right)


if __name__ == '__main__':
    alist = [3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]
    # alist = [3]
    # alist = [3, 9, 5, 6, 7, 8]
    print(merge_sort(random_arr0))
