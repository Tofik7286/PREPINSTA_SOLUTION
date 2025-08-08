# Check Whether a Number is Even or Odd in Python

# 1. Using Brute force attack
# num = int(input("Enter Number : "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 2. Ternary

# num = int(input("Enter Number : "))
# print("Even" if num % 2 == 0 else "Odd")


# Method 3 : Using Bitwise Operators


# def isEven(num):
#     return not num & 1


# num = int(input("Enter Number : "))
# if isEven(num):
#     print("Even")
# else:
#     print("Odd")


num = 33
if num & 1 == 0:
    print("Even")
else:
    print("Odd")
