# 7_Find_the_Greatest_of_the_Three_Numbers​
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num3 and num2 > num1:
    print(f"{num2} is greater")
elif num1 == num2 == num3:
    print("All are equal")
else:
    print(f"{num3} is greater")
