# Numerical Palindrome #1

# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:
#
# 2332
# 110011
# 54322345
#
# For a given number num, write a function to test if it's a numerical palindrome or not and return a boolean (true if it is and false if not). Return "Not valid" if the input is not an integer or less than 0.
#


class Test:
    def it(S):
        print(S)

    def assert_equals(a, b):
        print(a == b)


def palindrome(num): return ''.join(reversed(str(num))) == str(num) if isinstance(num, int) and num > -1 else "Not valid"


Test.assert_equals(palindrome(1221), True)
Test.assert_equals(palindrome(123322), False)
Test.assert_equals(palindrome("ACCDDCCA"), "Not valid")
Test.assert_equals(palindrome("1221"), "Not valid")
Test.assert_equals(palindrome(-450), "Not valid")
