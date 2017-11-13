# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
# 6kyu problem

# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more capitals letters. The 1st letter of a code is the capital letter of the book category. In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.
#
# In a given stocklist all codes have the same length and all numbers have their own same length (can be different from the code length).
#
# For example an extract of one of the stocklists could be:
#
# L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
# or
#
# L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"].
# In this stocklist all codes have a length of five and all numbers have a length of two.
#
# You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
#
#   M = {"A", "B", "C", "W"}
# or
#
#   M = ["A", "B", "C", "W"]
# and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.
#
# For the lists L and M of example you have to return the string (in Haskell/Clojure a list of pairs):
#
#   (A : 20) - (B : 114) - (C : 50) - (W : 0)
# where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.
#
# If L or M are empty return string is "" (Clojure should return an empty array instead).


class test():
    def assert_equals(a, b):
        print(a == b)


def stock_list(listOfArt, listOfCat):
    answer = {}
    listOfCat = sorted(listOfCat)
    listOfArt_splited = [i.split(' ') for i in listOfArt]

    for cat in listOfCat:
        for i in range(len(listOfArt_splited)):
            if cat in listOfArt_splited[i][0]:
                if cat in answer:
                    answer[cat] += int(listOfArt_splited[i][1])
                    listOfArt_splited[i][1] = 0
                else:
                    answer[cat] = int(listOfArt_splited[i][1])
                    listOfArt_splited[i][1] = 0

    string_to_return = ""
    for x, y in enumerate(sorted(answer)):
        if x == 0:
            string_to_return += "({} : {})".format(y, answer[y])
        else:
            string_to_return += " - ({} : {})".format(y, answer[y])
    return string_to_return


def stock_list(listOfArt, listOfCat):
    from collections import Counter
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join("({} : {})".format(cat, cnt[cat]) for cat in listOfCat)


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")
