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
