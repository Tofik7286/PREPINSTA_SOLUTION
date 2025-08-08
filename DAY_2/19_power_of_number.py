# Find the Power of a Number in Python Language
# Method 1: Using Pow() Function

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
print(pow(num1, num2))

# Method 2: Using Simple Iteration

print(f"Method 2 : {num1 ** num2}")


# 3. Recursion
def power_of_number(num, power):
    if power == 0:
        return 1
    return num * power_of_number(num, power - 1)


print(power_of_number(2, 3))
