# def binarySearch(arr, l, r, x, counter=0):
#     if l <= r:
#         mid = round(l + (r - l) / 2)
#         counter += 1
#         if arr[mid] == x:
#             return [mid, counter]
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid - 1, x, counter)
#         else:
#             return binarySearch(arr, mid + 1, r, x, counter)
#     else:
#         return -1
#
#
# arr = [*range(10000)]
# x = 40
# result = binarySearch(arr, 0, len(arr) - 1, x)
# print(result)


def binarySearch(List, Left, Right, Target, counter=0):
    if Left <= Right:
        mid = round(Left + (Right - Left) / 2)
        counter += 1
        if List[mid] == Target:
            return [mid, counter]
        elif List[mid] > Target:
            return binarySearch(List, Left, mid - 1, Target, counter)
        else:
            return binarySearch(List, mid + 1, Right, Target, counter)
    else:
        return -1


list0 = [*range(10093)]
t = 33

print(binarySearch(list0, 0, len(list0), t))
