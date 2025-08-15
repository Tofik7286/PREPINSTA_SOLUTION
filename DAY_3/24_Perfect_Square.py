# Check for Perfect Square in Python
import math
number = int(input("Enter Number "))

if (math.floor(math.sqrt(number)) == math.ceil(math.sqrt(number))):
    print("yes")
else:
    print("no")