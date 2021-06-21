# Hunter Barrows 1550107

# Coding Problem 2

import csv
import datetime

from datetime import date

user_input = input()

split = user_input.split(' ')
month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
Day = ('1,', '2,', '3,', '4,', '5,', '6,', '7,', '8,', '9,', '10,', '11,', '12,', '13', '14,', '15,', '16,', '17,', '18,', '19,', '20,', '21,', '22,', '23', '24,', '25,', '26,', '27,', '28,', '29,', '30,', '31,')
dict_month = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}
year = int(split[2])
year_range = range(2023)
today = date.today()
date_format = today.strftime("%m %d, %Y")
if split[0] in month_list and split[1] in Day and year in year_range:
    month = (dict_month.get(split[0]))
    split_from_comma = split[1].split(',')
    day = split_from_comma[0]
    year = str((split[2]))
    my_list = [month, day, year]
    print('/'.join(my_list))







