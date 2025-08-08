# Method 1: Using [1, number] as the Range

num = int(input("Enter Number :"))
for i in range(1, num):
    if num % i == 0:
        print(i, end=" ")
