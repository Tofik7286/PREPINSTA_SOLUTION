# Method 1:  Using Simple Iteration.

# rev = 0
# original_value = n
# while n != 0:
#     r = n % 10
#     rev = rev * 10 + r
#     n = n // 10
# if rev == original_value:
#     print("Palindrome")
# else:
#     print("Not")


# Method 2: Using String Slicing
n = int(input("Enter Number : "))
# rev = int((str(n)[::-1]))
# if rev == n:
#     print("Palindrome")
# else:
#     print("Not")


# Method 3: Using Recursion

def checkPalindrome(num, rev):
    if num == 0:
        return rev
    r = int(num % 10)
    rev = rev * 10 + r
    return checkPalindrome(num // 10, rev)


num = int(input("Enter Number : "))
rev = 0
rev = checkPalindrome(num, rev)
print("Palindrome" if rev == num else "Not")
