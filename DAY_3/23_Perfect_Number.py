# Perfect Number in Python
# number = int(input("Enter NUmber : "))
# sum = 0
# for i in range(1,number):
#     if number % i == 0:
#         sum = sum + i
# if sum == number:
#     print("yes")
# else:
#     print("no")


# Method 2 
number = int(input("Enter NUmber : "))
sum = 0
i = 1
while i < number:
    if number % i == 0:
        sum = sum + i
    i += 1


if sum == number:
    print("yes")
else:
    print("no")