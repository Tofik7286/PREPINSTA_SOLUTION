# Method 1: Using Iteration
num = int(input("Enter Number : "))
original_number = num
length = len(str(num))
sum = 0
while num != 0:
    r = num % 10
    num = num // 10
    sum += pow(r, length)
if original_number == sum:
    print("Armstrong")
else:
    print("Not")
