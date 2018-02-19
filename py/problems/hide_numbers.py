def hide_numbers(s):
    result = ''
    alist = list(s)
    for i in range(len(alist)):
        if i > 6:
            result += s[i]
        else:
            result += '*'
    return result


print("result : " + hide_numbers('01033334444'));


def hide_numbers(s):
    return "{}{}".format(len(s[:7]) * '*', s[7:])


print("result : " + hide_numbers('01033334444'));
