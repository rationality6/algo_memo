def countLetters(input):
    letterdict = {}
    sorted_list_input = sorted(list(input))
    result = ""

    for letter in sorted_list_input:
        letterdict[letter] = 0

    for letter in sorted_list_input:
        letterdict[letter] += 1

    for i in letterdict:
        result += "{}{}".format(i, letterdict[i])

    return result


print(countLetters("babdc"))
