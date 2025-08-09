# Check Whether a Number is Even or Odd in Python

num = int(input("Enter Number : "))

if num %2 == 0:
    print("Even")
else:
    print("Odd")

if num & 1 == 0:
    print("Even")
else:
    print("Odd")