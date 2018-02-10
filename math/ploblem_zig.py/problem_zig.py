# 문제
# "ab2v9bc13j5jf4jv21" => 9^2 + 13^2 + 5^2 + 21^2 = 716
# 
# 찾을수있는 가능한 패턴
# 1.숫자를 추출한다
# 2.짝수를 제외한 숫자들을 제곱한뒤 더한다

import re


class Test:
    def assert_equals(a, b):
        print(a == b)


secret_string = "ab2v9bc13j5jf4jv21"


def find_pattern(L): return sum(
    j ** 2 for j in [int(i) for i in re.findall(r'[\d]+', L)] if j % 2 != 0)


result = find_pattern(secret_string)
answer_cal_result = ((9**2) + (13**2) + (5**2) + (21**2))
Test.assert_equals(result, answer_cal_result)
