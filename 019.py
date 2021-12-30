"""
You are given the following information, but you may prefer
to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not
on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# 1 to 12 for Jan - Dec, and number of days in each
month_n = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# leap year dictionary.
month_l = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# number of months starting on a Sunday
count = 0

# start year
year = 1901

# 1901 starts on a Tuesday
day = 2

# find starting day of each month by adding the numbers of
# days in each month modulo 7. Each if elif elif else clause
# identifies whether the correspodning year is a leap year or not.
while year < 2001:
    if (((year % 100) == 0) & ((year % 400) == 0)):
        for i in range(1, 13):
            if day == 0:
                count += 1
            else:
                None
            day += month_l[i]
            day = day % 7
    elif (((year % 100) == 0) & ((year % 400) != 0)):
        for i in range(1, 13):
            if day == 0:
                count += 1
            else:
                None
            day += month_n[i]
            day = day % 7
    elif (year % 4) == 0:
        for i in range(1, 13):
            if day == 0:
                count += 1
            else:
                None
            day += month_l[i]
            day = day % 7
    else:
        for i in range(1, 13):
            if day == 0:
                count += 1
            else:
                None
            day += month_n[i]
            day = day % 7
    year += 1

print(count)

print(day)
