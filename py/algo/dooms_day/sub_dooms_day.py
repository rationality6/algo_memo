
def sub_dooms_day(month, day):
    dooms_day = [3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    day_array = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return day_array[(((dooms_day[month - 1]) - 3 + day) % 7)]


print(sub_dooms_day(1, 1))
