class Test:
    def assert_equals(self, anwser_code, anwser):
        print(anwser_code == anwser)


test = Test()


def find_nb(m):
    pass


test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
