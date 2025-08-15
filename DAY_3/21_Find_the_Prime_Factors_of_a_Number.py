# Find the Prime Factors of a Number 
def prime_factor(num):
    factors=[]
    factor = 2
    while num >=2:
        if num % factor == 0:
            factors.append(factor)
            num = num // factor
        else:
            factor += 1
    return factors

num = int(input("Enter Number : "))
print(prime_factor(num))

