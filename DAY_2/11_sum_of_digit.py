# Method 0: Using String Character Extraction


num = int(input("Enter Digit :"))
sum = 0
# for i in num:
#     sum = sum + int(i)
# print(sum)


# Method 1: Using Brute Force

while num != 0:
    r = num % 10
    sum = sum + r
    num = num // 10
# print(sum)


# Method 2: Using Recursion I
# def findSum(num, sum):
#     if num == 0:
#         return sum

#     r = num % 10
#     sum = sum + r
#     return findSum(num // 10, sum)


# print(findSum(num, sum))

# Method 3: Using Recursion II


def findSum(num, sum):
    if num == 0:
        return sum
    return (num % 10) + findSum(num // 10, sum)


print(findSum(num, sum))
