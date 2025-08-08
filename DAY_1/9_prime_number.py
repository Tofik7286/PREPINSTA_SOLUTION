# Prime Number

# 1. Simple If Else
num = int(input("Enter Number : "))
flag = 0
# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 1:
#     print("not Prime")
# else:
#     print("Prime")


# Method 2: Optimization by break condition


# if num < 2:
#     flag = 1
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             flag = 1
#             break
# if flag == 1:
#     print("Not Prime")
# else:
#     print("Prime")


# Method 3: Optimization by n/2 iterations

if num < 2:
    flag = 1
else:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            flag = 1
        else:
            flag = 0
if flag == 1:
    print("Not Prime ")
else:
    print("Prime")


# Method 4: Optimization by √n

if num < 2:
    flag = 1
else:
    for i in range(2, int(pow(num, 0.5))+1):
        if num % i == 0:
            flag = 1
        else:
            flag = 0
if flag == 1:
    print("Not Prime ")
else:
    print("Prime")


# Method 5: Basic Recursion technique
def isPrime(num, i=2):
    if num == i:
        return True
    if num < 2:
        return False
    if num % i == 0:
        return False
    return isPrime(num, i+1)


if isPrime(num) == True:
    print("Prime")
else:
    print("Not Prime")
