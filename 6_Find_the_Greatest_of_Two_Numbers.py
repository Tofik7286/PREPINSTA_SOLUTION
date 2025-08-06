# Find the Greatest of Two Numbers in Python

# 1. if else
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

# if num1 > num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")


# 2. Ternary

print(f"{num1} greater" if num1 > num2 else f"{num2} is greater")

# 3. Built in method

print(max(num1, num2))
