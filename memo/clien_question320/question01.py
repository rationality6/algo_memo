import csv


def duration_in_mins(datum, city):
    filename = ''
    victory = {}

    if city == 'SEOUL':
        filename = '2016.csv'
    elif city == 'BUSAN':
        filename = '2015.csv'
    else:
        filename = '2014.csv'

    with open(filename, 'r') as f_in:
        trip_reader = csv.DictReader(f_in)
        for row in trip_reader:
           1) victory.update(row)

        duration=None

        if city == 'NYC':
            2)duration=victory['tripduration']
            float(duration) / 60
        elif city == 'Chicago':
            2)duration=victory['tripduration']
            float(duration) / 60
        else:
            2)duration=victory['Duration (ms)']
            float(duration) / 60000

        return duration



if __name__ == "__main__":
    duration_in_mins(2, 'SEOUL')

# def duration_in_mins(datum, city):
#
#     filename = None
#     if city == 'SEOUL':
#         filename = '2016.csv'
#     elif city == 'BUSAN':
#         filename = '2015.csv'
#     else:
#         filename = '2014.csv'
#
#     victory = {}
#     with open(filename, 'r') as f_in:
#     trip_reader = csv.DictReader(f_in)
#     for row in trip_reader:
#        1) victory.update(row)
#
#
#
#     duration=None
#
#     if city == 'NYC':
#         2)duration=victory['tripduration']
#         float(duration) / 60
#     elif city == 'Chicago':
#         2)duration=victory['tripduration']
#         float(duration) / 60
#     else:
#         2)duration=victory['Duration (ms)']
#         float(duration) / 60000
#
#     return duration
