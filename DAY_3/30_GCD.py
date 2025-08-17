# Python program to find GCD of Two Numbers
n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
while n2!=0:
    n1,n2=n2,n1%n2
print(n1)