# Find the Greatest of Two Numbers in Python
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

if num1 > num2:
    print(f"{num1} is greater")
elif num1 == num2:
    print("Both are equal")
else:
    print(f"{num2} is greater")

print(f"{num1} is greater" if num1 > num2 else f"{num2} is greater")
