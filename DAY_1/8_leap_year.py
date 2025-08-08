# Leap year

# 1. using if else
import calendar
year = int(input("Enter Year (Format : YYYY) : "))
if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print("Leap")
else:
    print("Not leap")


# 2. Ternary
print("Leap" if (year % 400 == 0) or (year %
      4 == 0 and year % 100 != 0) else "Not leap")


# 3.  Using Calendar Module
print(calendar.isleap(year))

# 4. Lambda

# x = lambda year: "Leap" if (year % 400 == 0) or (year %4 == 0 and year % 100 != 0) else "Not Leap"
# print(x)
