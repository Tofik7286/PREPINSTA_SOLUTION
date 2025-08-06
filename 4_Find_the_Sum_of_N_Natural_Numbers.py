# Find the Sum of N Natural Numbers

# 1. for loop

num = int(input("Enter Number : "))
total = 0
for i in range(num+1):
    total += i
print(total)


# Method 2: Using the Formula
num = int(input("Enter Number : "))
print(int(num * (num + 1) / 2))

# 3. Recursion


def getSum(num):
    if num == 1:
        return 1
    return num + getSum(num-1)


num = int(input("Enter Number : "))
print(getSum(num))
