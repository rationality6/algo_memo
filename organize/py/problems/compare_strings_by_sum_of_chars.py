import re


def counter(S):
    if not S == None:
        if S.isalpha():
            return sum(ord(i) for i in S.upper())


def compare(s1, s2):
    return counter(s1) == counter(s2)

# def string_cnt(s):
#     try:
#         if s.isalpha():
#             return sum(ord(a) for a in s.upper())
#     except AttributeError:
#         pass
#     return 0
#
#
# def compare(s1, s2):
#     return string_cnt(s1) == string_cnt(s2)


print(compare("AD", "BC") == True)
print(compare("gf", "FG") == True)
print(compare("AD", "DD") == False)
print(compare("Ad", "DD") == False)
print(compare("zz1", "") == True)
print(compare("ZzZz", "ffPFF") == True)
print(compare("kl", "lz") == False)
print(compare(None, "") == True)
print(compare("!!", "7476") == True)
print(compare("##", "1176") == True)
