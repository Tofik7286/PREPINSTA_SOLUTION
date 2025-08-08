# python find prime numbers in range

low = int(input("Enter Initial value : "))
high = int(input("Enter Ending value : "))
primes = []
for i in range(low, high+1):
    flag = 0
    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(i)
print(primes)
