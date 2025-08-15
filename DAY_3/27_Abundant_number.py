# Check Whether or Not the Number is an Abundant Number in Python Language
def divisior(num):
    answer = [i for i in range(1,num) if num % i == 0]
    return sum(answer)

number = int(input("Enter Number : "))
answer = divisior(number)
if answer > number:
    print("Yes ")
else:
    print("No")