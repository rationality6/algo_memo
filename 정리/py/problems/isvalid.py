class Test:
    def assert_equals(a, b):
        print(a == b)


def valid_parentheses(string):
    stack = []
    dic = {")": "("}
    for i in string:
        if i in dic.values():
            stack.append(i)
        elif i in dic.keys():
            if stack == [] or stack.pop() != dic[i]:
                return False
    return not stack

# def valid_parentheses(s):
#     stack = []
#     dict = {"]": "[", "}": "{", ")": "("}
#     for char in s:
#         if char in dict.values():
#             stack.append(char)
#         elif char in dict.keys():
#             if stack == [] or dict[char] != stack.pop():
#                 return False
#     return stack == []


Test.assert_equals(valid_parentheses("  ("), False)
Test.assert_equals(valid_parentheses(")test"), False)
Test.assert_equals(valid_parentheses(""), True)
Test.assert_equals(valid_parentheses("hi())("), False)
Test.assert_equals(valid_parentheses("hi(hi)()"), True)
