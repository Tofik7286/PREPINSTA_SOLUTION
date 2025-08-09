# Prime Number

num = int(input("Enter NUmber : "))
flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
if flag == 0:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


def isPrime(num, i=2):
    if num == i:
        return True
    if num < 2:
        return False
    if num % i == 0:
        return False
    return isPrime(num, i+1)


if isPrime(num) == True:
    print("Prime")
else:
    print("Not Prime")
