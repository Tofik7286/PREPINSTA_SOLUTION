# 16_Find_the_Fibonacci_Series_up_to_Nth_Term

# Method 1: Using Simple Iteration

num = int(input("Enter Number : "))
n1, n2 = 0, 1
print(n1, n2, end=" ")
for i in range(2, num+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

# Method 2: Using Recursive Function


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)


print(f"\n0  1", end=" ")
for i in range(10):
    print(f"{fibo(i)}", end=" ")
