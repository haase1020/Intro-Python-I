# from student problem in help channel cs-34
from datetime import datetime


# accepts an arbitraty number of keyword arguments
def f4(**kwargs):
    # need to loop through args, pull out keys and values
    for key, value in kwargs.items():
        # print the keys and values
        if 'datetime.strptime' in str(value):
            print('key: {}, value: \"{}\"'.format(key, value))
        else:
            print('key: {}, value: {}'.format(key, value))


# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)
# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")
