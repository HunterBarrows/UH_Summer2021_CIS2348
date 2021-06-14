# Hunter Barrows 1550107

# Coding problem 1

print('Birthday Calculator')
print('Current Day')

# prompt user to enter current day
current_month = int(input('Month:'))
current_day = int(input('Day:'))
current_year = int(input('Year:'))

# prompt user to enter birth date
print('Birthday')

month_birth = int(input('Month:'))
day_birth = int(input('Day:'))
year_birth = int(input('Year:'))

age_day = current_day - day_birth
age_month = current_month - month_birth
age_year = current_year - year_birth

if current_month > month_birth and current_day > day_birth:
    age_year == age_year
elif current_month == month_birth:
    age_year == age_year
elif current_day == day_birth:
    age_year == age_year
else:
    age_year -= 1


if current_month == month_birth and current_day == day_birth:
    print('Happy Birthday')
    print('You are', age_year, 'years old.')
else:
    print('You are', age_year, 'years old.')