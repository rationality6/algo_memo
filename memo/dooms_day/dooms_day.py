# dooms_days = [
#     "4/4",
#     "6/6",
#     "8/8",
#     "10/10",
#     "12/12",
#     "5/9",
#     "9/5",
#     "7/11",
#     "11/7"
# ]
# week = [
#     "화요일",
#     "수요일",
#     '목요일',
#     '금요일',
#     '토요일',
#     '일요일',
#     '월요일'
# ]
#
#
# def leap_year_checker(year):
#     year -= 2000
#     first = year / 12
#     second = year % 12
#     thirth = second / 4
#     return (first + second + thirth) % 7
#
#
# def dooms_day_checker(arg):
#     splited_arg = arg.split("/")
#     num = int(leap_year_checker(int(splited_arg[0])))
#     the_week = week[num]
#
#     for i in dooms_days:
#         if i == "{}/{}".format(splited_arg[1], splited_arg[2]):
#             return "It's dooms_day {}".format(the_week)
#
#
# print(dooms_day_checker("2017/9/5"))

dooms_days_obj = {
    1: '3',
    2: '28',
    4: '4',
    5: '9',
    6: '6',
}
for i in dooms_days_obj:
    print(dooms_days_obj[i])

# [
#     "4/4",
#     "6/6",
#     "8/8",
#     "10/10",
#     "12/12",
#     "5/9",
#     "9/5",
#     "7/11",
#     "11/7"
# ]
#
