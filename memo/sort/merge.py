def merge(left, right):
    result = []
    i, j = 0, 0
    # iterate through both arrays and arrange the elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

# The loop may break before all elements are copied hence append the remaining elements
    result += left[i:]
    result += right[j:]
    return result


# The mergesort method to split the arrays into smaller subarrays
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    print(left)
    right = mergesort(lst[middle:])
    return merge(left, right)


if __name__ == '__main__':
    alist = [3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]
    # alist = [3]
    # alist = [3, 9, 5, 6, 7, 8]
    print(mergesort(alist))
