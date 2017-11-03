import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


def partitioning(List, Start, End):
    pivot = List[Start]
    left = Start + 1
    right = End
    done = False
    while not done:
        while left <= right and List[left] <= pivot:
            left += 1
        while left <= right and List[right] >= pivot:
            right -= 1
        if left > right:
            done = True
        else:
            List[left], List[right] = List[right], List[left]
    List[Start], List[right] = List[right], List[Start]
    return right


def quick_sort_hoare(List, Start, End):
    if Start < End:
        pivot = partitioning(List, Start, End)
        quick_sort_hoare(List, Start, pivot - 1)
        quick_sort_hoare(List, pivot + 1, End)
    return List


if __name__ == "__main__":
    # random_arr0 = random_arr(0, 10)
    # random_arr0 = random_arr(0, 5)
    random_arr0 = [2, 1, 4, 5, 3]
    # random_arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print(random_arr0, 'start')
    print(quick_sort_hoare(random_arr0, 0, len(random_arr0) - 1), 'end')
