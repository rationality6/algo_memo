# Simple interest on a loan is calculated by simply taking the initial amount (the principal, P) and multiplying it by a rate of interest (r) and the number of time periods (n).
#
# Compound interest is calculated by adding the interest after each time period to the amount owed, then calculating the next interest payment based on the principal PLUS the interest from all previous periods.
#
# Given a principal P, interest rate r, and a number of periods n, return an array [total owed under simple interest, total owed under compound interest].
#
# EXAMPLES:
#
# interest(100,0.1,1) = [110,110]
# interest(100,0.1,2) = [120,121]
# interest(100,0.1,10) = [200,259]
# Round all answers to the nearest integer. Principal will always be an integer between 0 and 9999; interest rate will be a decimal between 0 and 1; number of time periods will be an integer between 0 and 49.
#


class Test:
    def assert_equals(answer_func, answer):
        print(answer_func == answer)

    def it(n):
        print(n)


def interest(p, r, t):
    print([int(p + p * r * t), int(p * (1 + r)**t)])
    return[int(p + p * r * t), int(p * (1 + r)**t)]


Test.it('STATIC TESTS')
Test.assert_equals(interest(100, 0.1, 1), [110, 110])
# Test.assert_equals(interest(100, 0.1, 2), [120, 121])

print(len([i for i in range(1, 101) if i % 3 == 0 or i % 2 == 0]))


def func0(x):
    return x**2 if x % 2 == 0 else x + 5
print(func0(2))
print(func0(3))

print(100*1.1**12)
print(100+100*0.1*12)
