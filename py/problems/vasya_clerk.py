class Test:
    def assert_equals(self, anwser_code, anwser, *args):
        print(anwser_code == anwser)

    def expect(self, anwser_code, anwser, *args):
        print(anwser_code == anwser)


test = Test()


def tickets(people):
    wallet = {100: 0, 50: 0, 25: 0}
    for paid in people:
        wallet[paid] += 1
        change = paid - 25
        for bill in (50, 25):
            while bill <= change and wallet[bill] > 0:
                wallet[bill] -= 1
                change -= bill
        if change != 0:
            return "NO"
    return "YES"


test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
