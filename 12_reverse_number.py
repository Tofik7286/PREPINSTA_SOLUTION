# Method 1: Using Simple Iteration


num = int(input("Enter Number : "))
rev = 0
while num != 0:
    r = num % 10
    num = num // 10
    rev = rev * 10 + r
print(rev)


# Method 2: Using String Slicing
num = input("Enter Number : ")
print(num[::-1])


# Method 3: Using Recursion
def findRev(num, rev):
    if num == 0:
        return rev
    r = num % 10
    rev = rev * 10 + r
    return findRev(num // 10, rev)


num = int(input("Enter Number : "))
rev = 0
print(findRev(num, rev))


# Method 4 using string

x = "99659"
r = ""
for i in x:
    r = i + r
print(r)
