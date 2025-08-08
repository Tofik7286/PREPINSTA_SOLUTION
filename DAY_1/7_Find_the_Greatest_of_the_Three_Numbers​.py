# 7_Find_the_Greatest_of_the_Three_Numbers​

# 1. if else
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")


# 2. Ternary

max = num1 if num1 > num2 else num2
max = num3 if num3 > max else max
print(max)
