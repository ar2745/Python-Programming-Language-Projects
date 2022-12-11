import calendar

year = input('Please insert a year to check if it is a leap year:  ')
month = input('Please insert the month of the year you entered to see that calendar month: ')
if calendar.isleap(True == int(year)):
    print('\n', calendar.isleap(int(year)), year, 'is a leap year')
elif calendar.isleap(False == int(year)):
    print('\n', calendar.isleap(int(year)), year, ' is not a leap year')

print('\n', calendar.month(int(year), int(month)))

print('\n', calendar.calendar(int(year)))