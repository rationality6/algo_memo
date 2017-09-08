from collections import Counter
result = ""
col0 = Counter(list("biiua"))
for i in sorted(col0):
    result += ("{}:{}".format(i, col0[i]))
print(result)
