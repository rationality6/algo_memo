stick_prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

sub0 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def maximum_subarray(L):
    max_ending_here = L[0]
    max_so_far = L[0]
    for i in L[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# print(max_subarray(stick_prices))
# print(maximum_subarray(stick_prices))
print(maximum_subarray(sub0))
