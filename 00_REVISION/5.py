# Find the Sum of Numbers in a given Range in Python
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
total = 0

for i in range(num1, num2+1):
    total += i
print(total)

print((num2 * (num2+1) / 2) - (num1 * (num1+1) / 2) + num1)
