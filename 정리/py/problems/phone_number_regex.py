class Test:
    def assert_equals(a, b):
        print(a == b)


def validPhoneNumber(phoneNumber):
    import re
    rec = re.compile('\d')

    for i in range(len(phoneNumber)):
        if i == 0:
            if phoneNumber[i] != "(":
                return False
        elif i == 4:
            if phoneNumber[i] != ")":
                return False
        elif i == 5:
            if phoneNumber[i] != " ":
                return False
        elif i == 9:
            if phoneNumber[i] != "-":
                return False
        else:
            if rec.match(phoneNumber[i]):
                pass
            else:
                return False
    return True


def validPhoneNumber(phoneNumber):
    import re
    print(bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$" , phoneNumber)))
def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))

# def validPhoneNumber(phoneNumber):
#     import re
#     rec = re.match(r'(\(\d+\))',phoneNumber)
#     print(bool(rec))
validPhoneNumber("239048")
validPhoneNumber("(123) 456-7890")

# Test.assert_equals(validPhoneNumber("(123) 456-7890"), True)
# Test.assert_equals(validPhoneNumber("(1111)555 2345"), False)
# Test.assert_equals(validPhoneNumber("(098) 123 4567"), False)
