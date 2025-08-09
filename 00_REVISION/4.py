# Find the Sum of N Natural Numbers
num = int(input("Enter Number : "))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print(sum)

print(int(num * (num+1)/2))


def getSum(num):
    if num == 0:
        return 0
    return num + getSum(num-1)


print(getSum(num))
