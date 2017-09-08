import collections

result = ""
string0 = "hello"
c = collections.Counter(list(string0))
for i in sorted(c):
    result += "{}{}".format(i, c[i])
print(result)
