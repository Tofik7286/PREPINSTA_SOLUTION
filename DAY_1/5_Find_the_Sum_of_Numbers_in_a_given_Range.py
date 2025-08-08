# Find the Sum of Numbers in a given Range in Python

# 1. Using Brute Force
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
total = 0

# for i in range(num1, num2+1):
#     total += i
# print(total)


# 2. Using Method

print((num2 * (num2 + 1) / 2) - (num1 * (num1+1)/2) + num1)


# 3. Using Recursion

def recurSum(num1, num2):
    if num1 > num2:
        return 0
    return num1 + recurSum(num1 + 1, num2)


print(recurSum(num1, num2))
