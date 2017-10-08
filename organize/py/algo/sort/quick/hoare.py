import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


def test(ran_func, length, anwser_func):
    is_work = True
    for i in range(length):
        ran0 = ran_func(0, i)
        ran1 = ran0[:]
        posts = anwser_func(ran0, 0, len(ran0) - 1)
        anwser = sorted(ran1)
        if posts != anwser:
            is_work = False
    return is_work


def partition(LIST, start, end):
    pivot = LIST[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and LIST[left] <= pivot:
            left += 1
        while left <= right and pivot <= LIST[right]:
            right -= 1
        if left > right:
            done = True
        else:
            LIST[left], LIST[right] = LIST[right], LIST[left]
    LIST[start], LIST[right] = LIST[right], LIST[start]
    return right


def quick_sort(alist, start, end):
    if start < end:
        pivot = partition(alist, start, end)
        quick_sort(alist, start, pivot - 1)
        quick_sort(alist, pivot + 1, end)
    return alist


if __name__ == "__main__":
    myList = random_arr(0, 10)
    # myList = [7, 2, 5, 1, 29, 6, 4, 19, 11]
    # myList = [1, 7, 2, 8, 9, 6, 5, 3, 4, 0]

    print(myList, 'start')

    sortedList = quick_sort(myList, 0, len(myList) - 1)
    print(sortedList, 'end')
    print(test(random_arr, 100, quick_sort))
