# Check Whether or Not the Number is an Automorphic Number in Python Language
# number = int(input("Enter NUmber : "))
# flag= 0
# sqaure = number* number
# original_number_square = sqaure
# n = 10
# while sqaure!=0:
#     r = sqaure % n
#     if r == number:
#         break
#     sqaure = sqaure // 10
#     n = n * 10
# if flag == 1:
#     print("Yes")
# else :
#     print("no")


# 2. 

number = int(input("Enter NUmber : "))
a = str(number)
square = number * number
b = str(square)
if b.endswith(a):
    print("yes")
else:
    print("no")