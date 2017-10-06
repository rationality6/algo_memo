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
    # myList = [7, 2, 5, 1, 29, 6, 4, 19, 11]
    myList = [1, 7, 2, 8, 9, 6, 5, 3, 4, 0]
    print(myList, 'start')
    sortedList = quick_sort(myList, 0, len(myList) - 1)
    print(sortedList, 'end')
