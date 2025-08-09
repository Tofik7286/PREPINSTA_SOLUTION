# Leap Year
import calendar
year = int(input("Enter Year (Format : YYYY) : "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is leap ")
else:
    print(f"{year} is not leap ")


print(calendar.isleap(year))
if calendar.isleap(year):
    print("yes it is leap year")
else:
    print("No")
