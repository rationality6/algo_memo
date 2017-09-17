def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        # max_ending_here = max(x, max_ending_here + x)
        # max_so_far = max(max_so_far, max_ending_here)

        # 1 = max(1, -2 + 1)
        # -2 = max(-2, 1)

        # 4 = max(4, -2 + 4)
        # 4 = max(-2, 4)

        # 3 = max(-1, 4 + -1)
        # 4 = max(4, 3)

        # 5 = max(2, 3 + 2)
        # 5 = max(4, 5)

        # 6 = max(1, 5 + 1)
        # 6 = max(5, 6)

        # 1 = max(-5, 6 + -5)
        # 6 = max(6, 1)

        # 5 = max(4, 1 + 4)
        # 6 = max(6, 5)
    return max_so_far


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(ex))


def max_subarray(A):
    m = s = A[0]
    for x in A[1:]:
        m = max(x, m + x)
        s = max(s, m)
    return s


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(ex))


# brute force solution o(n^2)
def max_subarray(A):
    length = len(A)
    maxium = 0
    result = ""
    for x in range(length):
        for y in range(length):
            value = sum(ex[x:y])
            if(value > maxium):
                maxium = value
                result = "{} [{}:{}]".format(maxium, x, y)
    return result


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(ex))


def maxSubArraySum(arr):
    m = s = arr[0]
    for i in range(1, len(arr)):
        m = max(arr[i], m + arr[i])
        s = max(s, m)
    return s


arr0 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(arr0))
