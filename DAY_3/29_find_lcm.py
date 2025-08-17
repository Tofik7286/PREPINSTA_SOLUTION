# n1 = int(input("Enter Number 1 : "))
# n2 = int(input("Enter Number 2 : "))
# maxNumber = max(n1,n2)
# while True:
#     if (maxNumber % n1==0 and maxNumber % n2 == 0):
#         break
#     maxNumber +=1
# print(maxNumber)

# LCM more than 2 numbers
def LCM(n1,n2):
    maxNumber = max(n1,n2)
    while True:
        if maxNumber % n1 == 0 and maxNumber % n2 == 0:
            break
        maxNumber+=1
    return maxNumber

n = int(input("Enter Number : "))
l = []
for i in range(n):
    l.append(int(input("Enter Number  : ")))
lcm=l[0]
for i in range(0,len(l)):
    lcm = LCM(lcm,l[i])
print(lcm)