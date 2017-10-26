# 링크

# https://www.codewars.com/kata/fizz-buzz/python

# 문제

# Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1 (in C#, N might be less then 1).
#
# C# ONLY: If N is smaller then or equal to 0, throw an ArgumentOutOfRangeException!
# Replace certain values however if any of the following conditions are met:
#
# If the value is a multiple of 3: use the value 'Fizz' instead
# If the value is a multiple of 5: use the value 'Buzz' instead
# If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead
# C# method calling example:

# string[] result = FizzBuzz.GetFizzBuzzArray(3); // => [ "1", "2", "Fizz" ]


class test:
    def describe(S):
        # print(S)
        pass

    def it(S):
        # print(S)
        pass

    def assert_equals(a, b):
        # print(a)
        print(a == b)


# def fizzbuzz(n):
#     # your code here
#     result = []
#     for i in range(1, n + 1):
#         if i % 5 == 0 and i % 3 == 0:
#             result.append("FizzBuzz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         else:
#             result.append(i)
#     return result

def fizzbuzz(n):
    # your code here
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, n + 1)]


test.describe('Fizzbuzz')
test.it('Should fizzify 10 numbers correctly')
expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
test.assert_equals(fizzbuzz(10), expected)
