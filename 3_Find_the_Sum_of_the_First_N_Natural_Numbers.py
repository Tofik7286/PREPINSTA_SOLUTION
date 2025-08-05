# Find the Sum of the First N Natural Numbers in Python

# 1. For loop
num = int(input("Enter Number :"))
total = 0
for i in range(num+1):
    total += i
print(total)


# Method 2 : Using Formula for the Sum of Nth Term
print(int(num * (num+1) / 2))


# Method 3 : Using Recursion

def getSum(num):
    if num == 1:
        return 1

    return num + getSum(num-1)


print(getSum(num))
