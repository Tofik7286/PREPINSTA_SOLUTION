# 17_Find_the_Nth_Term_of_a_Fibonacci_Series
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)


n = int(input("Enter NUmber :"))
print(fibo(n-1))
