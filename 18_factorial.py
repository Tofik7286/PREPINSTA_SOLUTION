# num = int(input("Enter Number : "))
# mul = 1
# for i in range(1, num+1):
#     mul = mul * i

# print(mul)
# Time complexity: O(N)
# Space complexity: O(1)


# Method 2 (Recursive)

def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


num = int(input("Enter Number : "))

print(fact(num))
