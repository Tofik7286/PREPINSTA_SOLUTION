# Positive or Negative number:
# we have three methods to solve this

# 1. Brute- force method
# num = int(input("Enter Number : "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# 2. Using Nested if-else
# num = int(input("Enter Number : "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive")
# else:
#     print("Negative")


# 3. Ternary
num = int(input("Enter Number : "))
print("Positive" if num >= 0 else "Negative")
