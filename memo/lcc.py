# longerst consecutive character


def lcc(seq):

    max_count = 1
    max_char = ''
    result = 1
    result_dic = {}

    split_seq = list(seq)

    for i in range(1, len(split_seq)):
        if split_seq[i] == split_seq[i - 1]:
            max_count += 1
        else:
            max_count = 1
        if result < max_count:
            result = max_count
            max_char = split_seq[i]
    result_dic["{}".format(max_char)] = result
    return result_dic


print(lcc("AABCDDBBBEA"))


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
        max_ending = max(i, max_ending + i)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(ex))
