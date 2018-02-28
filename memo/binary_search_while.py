# let arrOne = [1, 2, 3, 4, 5, 6]

arrOne = [1, 2, 3, 4, 5, 6, 7]


def binarySearch(L, D):
    begin = 0
    end = len(L)
    while begin < end:
        mid = begin + (end - begin) // 2

        if L[mid] == D:
            return mid
        elif L[mid] < D:
            begin = mid
        else:
            end = mid


print(binarySearch(arrOne, 7))


# swift

# func binarySearch(_ inputArray: [Int], element: Int) -> Int? {
#
#     var begin = 0
#     var end = inputArray.count
#
#     while begin < end {
#         let mid = begin + (end - begin) / 2
#
#         if inputArray[mid] == element {
#             return mid
#         } else if inputArray[mid] < element {
#             begin = mid
#         } else {
#             end = mid
#         }
#
#     }
#
#     return nil
# }
#
# binarySearch([1, 2, 3, 4, 5], element: 2)
