import collections
result = ""
col0 = collections.Counter(list("biiua"))
for i in sorted(col0):
    result += ("{}:{}".format(i, col0[i]))
print(result)
