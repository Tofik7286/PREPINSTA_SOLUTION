# Harshad NUmber 
number = int(input("Enter Number :"))
original_number = number
sum_of_digits = 0
while number !=0:
    r = number % 10
    sum_of_digits = sum_of_digits + r
    number = number // 10
print(sum_of_digits)
if original_number % sum_of_digits == 0:
    print("yes")
else:
    print("no")