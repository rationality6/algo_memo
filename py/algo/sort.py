def bubble_sort(L):
    for i in reversed(range(len(L))):
        for j in range(i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


list0 = [*reversed(range(5))]
print(list0)
print(bubble_sort(list0))


def selection_sort(L):
    for i in range(len(L)):
        index = i
        for j in range(i + 1, len(L)):
            if L[index] > L[j]:
                index = j
        L[i], L[index] = L[index], L[i]
    return L


list0 = [*reversed(range(5))]
print(list0)
print(selection_sort(list0))


def insertion_sort(L):
    for i in range(1, len(L)):
        position = i
        current = L[i]
        while 0 < position and current < L[position - 1]:
            L[position] = L[position - 1]
            position -= 1
        L[position] = current
    return L


list0 = [*reversed(range(5))]
print(list0)
print(insertion_sort(list0))


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


def merge_sort(L):
    if len(L) <= 1:
        return L
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)


list0 = [*reversed(range(5))]
print(list0)
print(merge_sort(list0))


def quick_sort(L, start, end):
    pass
