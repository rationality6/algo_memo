def sort(alist):
    for i in range(1, len(alist)):
        pos = i
        current = alist[i]
        while pos > 0 and alist[pos - 1] > current:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = current


# ls0 = [1, 2, 3, 4, 5]
ls0 = [8, 5, 6, 7, 9, 1, 2, 3, 4]
# ls0 = [9, 8, 6, 7]

sort(ls0)
print(ls0)


# 1 > 0 and alist[1 - 1] > 2:
# True and 1 > 2
# 1 > 0 and 4 > 5:
# True and 4 > 5:


def sort_numbers(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j + 1] = s[j]
            j = j - 1
        s[j + 1] = val


alist = [5, 3, 7, 8, 9, 1, 2, 4, 6]
print(sort_numbers(alist))
print(alist)
