# A very passive-aggressive co-worker of yours was just fired. While he was gathering his things, he quickly inserted a bug into your system which renamed everything to what looks like jibberish. He left two notes on his desk, one reads: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" while the other reads: "Uif usjdl up uijt lbub jt tjnqmf kvtu sfqmbdf fwfsz mfuufs xjui uif mfuufs uibu dpnft cfgpsf ju".
#
# Rather than spending hours trying to find the bug itself, you decide to try and decode it.
#
# If the input is not a string, your function must return "Input is not a string". Your function must be able to handle capital and lower case letters. You will not need to worry about punctuation.


class Test:
    def assert_equals(result, awswer):
        print(result == awswer)


def one_down(txt):
    if type(txt) != str:
        return "Input is not a string"
    else:
        new_txt = ""
        for i in txt:
            if i == ' ':
                new_txt += " "
            elif i == 'A':
                new_txt += "Z"
            elif i == 'a':
                new_txt += "z"
            elif i in "-+,.;:":
                new_txt += i
            else:
                new_txt += chr(ord(i) - 1)
        print(new_txt)
        return new_txt


def one_down(txt):
    def rotate_right(txt):
        return txt[-1] + txt[:-1]
    if not isinstance(txt, str):
        return "Input is not a string"
    return txt.translate(string.maketrans(
        string.ascii_uppercase + string.ascii_lowercase,
        rotate_right(string.ascii_uppercase) + rotate_right(string.ascii_lowercase)))


Test.assert_equals(one_down("Ifmmp"), "Hello")
Test.assert_equals(one_down("Uif usjdl up uijt lbub jt tjnqmf"),
                   "The trick to this kata is simple")
Test.assert_equals(one_down(45), "Input is not a string")
Test.assert_equals(one_down("XiBu BcPvU dSbAz UfYu"), "WhAt AbOuT cRaZy TeXt")
Test.assert_equals(one_down(["Hello there", "World"]), "Input is not a string")
