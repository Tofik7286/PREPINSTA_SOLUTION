# Check Whether or Not the Number is a Strong Number
def fact(r):
    mul = 1
    for i in range(1,r+1):
        mul = mul * i
    return mul
number = int(input("Enter Number : "))
original_number= number
strong = 0
while number!=0:
    r = number % 10
    factorial =  fact(r)
    strong += factorial
    number = number // 10

if original_number == strong:
    print("Yes")
else:
    print("No")