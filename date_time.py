# Working with dates and times
# Many interesting data sets have a date or time as the x-
# value. Python’s datetime module helps you work with this
# kind of data.
from datetime import datetime as dt

today=dt.now()
date_string = dt.strftime(today, '%m/%d/%y')
print(date_string )

print('\n# Generating a specific date')
# You can also generate a datetime object for any date and time you
# want. The positional order of arguments is year, month, and day.
# The hour, minute, second, and microsecond arguments are
# optional.
new_years=dt(2019,1,1)
print(new_years)
fall_equinox=dt(year=2017,month=9,day=22)
print(fall_equinox)

# Datetime formatting arguments
# The strftime() function generates a formatted string from a
# datetime object, and the strptime() function genereates a
# datetime object from a string. The following codes let you work with
# dates exactly as you need to.
# %A  Weekday name, such as Monday
# %B  Month name, such as January
# %m  Month, as a number (01 to 12)
# %d  Day of the month, as a number (01 to 31)
# %Y  Four-digit year, such as 2016
# %y  Two-digit year, such as 16
# %H  Hour, in 24-hour format (00 to 23)
# %I  Hour, in 12-hour format (01 to 12)
# %p  AM or PM
# %M  Minutes (00 to 59)
# %S  Seconds (00 to 61)

print('\n# Converting a string to a datetime object')
new_year_obj = dt.strptime('2/2/2010', '%m/%d/%Y') # Y instead of y
print(new_year_obj)
print('\n# Converting a datetime object to a string')
new_year_str=dt.strftime(new_year_obj, '%B %d,%Y')
print(new_year_str)
