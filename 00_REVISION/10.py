# python find prime numbers in range
low = int(input("Enter Initial value : "))
high = int(input("Enter Ending value : "))
primes = []
for i in range(low, high+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    else:
        primes.append(i)
print(primes)
