def brute_force(arr):
    max_val = 0
    max_arr = []
    for i in range(len(arr)):
        for z in range(len(arr)):
            sum_value = sum(arr[i:z])
            if max_val < sum_value:
                max_val = sum_value
                max_arr = arr[i:z]
    return "{} : {}".format(max_val, max_arr)


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(brute_force(ex))


def kadane(ARR):
    max_ending = max_so_far = ARR[0]
    for i in ARR[1:]:
        max_ending = max(0, max_ending + i)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(ex))
