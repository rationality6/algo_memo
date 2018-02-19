import random


def random_arr(a, b):
    arr0 = [*range(a, b)]
    for i in range(len(arr0)):
        rn = random.randint(0, len(arr0) - 1)
        arr0[i], arr0[rn] = arr0[rn], arr0[i]
    return arr0


def test(ran_func, length, anwser_func):
    is_work = True
    for i in range(length):
        ran0 = ran_func(0, i)
        posts = anwser_func(ran0)
        anwser = sorted(ran0)
        if posts != anwser:
            is_work = False
    return is_work


def test_for_quick(ran_func, length, anwser_func):
    is_work = True
    for i in range(length):
        ran0 = ran_func(0, i)
        posts = anwser_func(ran0, 0, len(ran0) - 1)
        anwser = sorted(ran0)
        if posts != anwser:
            is_work = False
    return is_work


def merge(left, right):
    result = []
    r, l = 0, 0
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


def merge_sort(N):
    if len(N) <= 1:
        return N
    middle = len(N) // 2
    left = merge_sort(N[:middle])
    right = merge_sort(N[middle:])
    return merge(left, right)


def selection_sort(N):
    clone = N[:]
    n_length = len(clone)
    for i in range(n_length):
        index = i
        for z in range(i + 1, n_length):
            if clone[index] > clone[z]:
                index = z
        clone[i], clone[index] = clone[index], clone[i]
    return clone


def bubble_sort(N):
    clone_n = N[:]
    for i in reversed(range(len(clone_n))):
        for z in range(i):
            if clone_n[z] > clone_n[z + 1]:
                clone_n[z], clone_n[z + 1] = clone_n[z + 1], clone_n[z]
    return clone_n


def insertion_sort(N):
    NN = N[:]
    for i in range(1, len(NN)):
        cur = NN[i]
        p = i
        while p > 0 and cur < NN[p - 1]:
            NN[p] = NN[p - 1]
            p -= 1
        NN[p] = cur
    return NN


def partition(LIST, START, END):
    pivot = LIST[START]
    left = START + 1
    right = END
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
    LIST[START], LIST[right] = LIST[right], LIST[START]
    return right


def quick_sort(LIST, start, end):
    if start < end:
        pivot = partition(LIST, start, end)
        quick_sort(LIST, start, pivot - 1)
        quick_sort(LIST, pivot + 1, end)
    return LIST


if __name__ == '__main__':
    arr0 = random_arr(0, 10)
    print(arr0)

    # print(insertion_sort(arr0))
    # print(bubble_sort(arr0))
    # print(selection_sort(arr0))
    # print(merge_sort(arr0))
    print(quick_sort(arr0, 0, len(arr0) - 1))

    # test
    # print(test(random_arr, 100, insertion_sort))
    # print(test(random_arr, 100, bubble_sort))
    # print(test(random_arr, 100, selection_sort))
    # print(test(random_arr, 100, merge_sort))
    print(test_for_quick(random_arr, 100, quick_sort))
