class Dooms_day_machine():
    def __init__(self):
        self.dooms_days = {
            1: '3',
            2: '28',
            4: '4',
            5: '9',
            6: '6',
            7: '11',
            8: '8',
            9: '5',
            10: '10',
            11: '7',
            12: '12',
        }
        self.days_in_korean = ["일", "월", "화", "수", "목", "금", "토"]

    def standard_day_checker(self, year):
        if year < 1900:
            print('Too low')
        elif year > 2299:
            print('Too high')
        else:
            if year >= 1900 and year <= 1999:
                print("1900-1999")
                return 3
            elif year >= 2000 and year <= 2099:
                print("2000-2099")
                return 2
            elif year >= 2100 and year <= 2199:
                print("2100-2199")
                return 0
            else:
                print("2200-2299")
                return 5

    def do_subtrack_year(self, year):
        listed_year = list(str(year))
        return int("{}{}".format(listed_year[2], listed_year[3]))

    def leap_year_checker(self, year):
        standard_year_num = self.standard_day_checker(year)
        year_postfix = self.do_subtrack_year(year)
        first = int(year_postfix / 12)
        second = int(year_postfix % 12)
        thirth = int(second / 4)
        result = int(first + second + thirth + standard_year_num) % 7
        return result

    def dooms_day_checker(self, arg):
        splited_arg = arg.split("/")
        num = self.leap_year_checker(int(splited_arg[0]))
        day = int(splited_arg[2])

        for i in self.dooms_days:
            if(i == int(splited_arg[1])):
                print(self.dooms_days[i], 'self.dooms_days[i]')
                print(day, 'day')
                print(num)
                result = (num + day - int(self.dooms_days[i])) % 7
                return self.days_in_korean[result]


machine0 = Dooms_day_machine()
print(machine0.dooms_day_checker("2017/1/22"))
