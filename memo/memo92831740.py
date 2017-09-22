import random


def random_arr(a, b):
    arr0 = [*range(a, b)]
    for i in range(len(arr0)):
        rn = random.randint(0, len(arr0) - 1)
        arr0[i], arr0[rn] = arr0[rn], arr0[i]
    return arr0


def insertion_sort(LIST):
    clone = LIST[:]
    for i in range(1, len(clone)):
        current = clone[i]
        position = i
        while position > 0 and current < clone[position - 1]:
            clone[position] = clone[position - 1]
            position -= 1
        clone[position] = current
    return clone


def bubble_sort(LIST):
    clone = LIST[:]
    for i in reversed(range(1, len(clone))):
        for z in range(i):
            if clone[z] > clone[z + 1]:
                clone[z], clone[z + 1] = clone[z + 1], clone[z]
    return clone


def selection_sort(LIST):
    clone = LIST[:]
    length = len(clone)
    for i in range(length - 1):
        index = i
        for z in range(i + 1, length):
            if clone[index] > clone[z]:
                index = z
        clone[index], clone[i] = clone[i], clone[index]
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
    if len(LIST) <= 1:
        return LIST
    middle = len(LIST) // 2
    left = merge_sort(LIST[:middle])
    right = merge_sort(LIST[middle:])
    return merge(left, right)


def test(ran_func, length, anwser_func):
    is_work = True
    for i in range(length):
        ran0 = ran_func(0, i)
        posts = anwser_func(ran0, 0, len(ran0) - 1)
        anwser = sorted(ran0)
        if posts != anwser:
            is_work = False
    return is_work

#
# def partition():
#     pivot = LIST[start]
#     left = start + 1
#     right = end
#     done = False
#     while not done:
#         while left <= right and LIST[left] <= pivot:
#             left += 1
#         while left <= right and LIST[right] >= pivot
#             right -= 1
#         if right < left:
#             done = True
#         else:
#             LIST[left], LIST[right] = LIST[right], LIST[left]
#
#
# def quick_sort(LIST, start, end):
#     if start < end:
#         pivot = partition(LIST, start, end)
#         quick_sort(LIST, start, pivot - 1)
#         quick_sort(LIST, pivot + 1, end)
#     return LIST


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
        if right < left:
            done = True
        else:
            LIST[left], LIST[right] = LIST[right], LIST[left]
    LIST[start], LIST[right] = LIST[right], LIST[start]
    return right


def quick_sort(LIST, start, end):
    if start < end:
        pivot = partition(LIST, start, end)
        quick_sort(LIST, start, pivot - 1)
        quick_sort(LIST, pivot + 1, end)
    return LIST


if __name__ == '__main__':
    arr0 = random_arr(0, 15)
    print(arr0)

    # print(insertion_sort(arr0))
    # print(bubble_sort(arr0))
    # print(selection_sort(arr0))
    # print(merge_sort(arr0))
    print(quick_sort(arr0, 0, len(arr0) - 1))

    # test
    # print(test(random_arr, 100, bubble_sort))
    # print(test(random_arr, 100, insertion_sort))
    # print(test(random_arr, 100, selection_sort))
    # print(test(random_arr, 100, merge_sort))
    # print(test(random_arr, 100, quick_sort))


print(format(("0000111101010101010"), '0d'))
a = "0000111101010101010"
print(int(a, 2))


a=20
def A():
    print(a)
a=10
print(a)
A()
