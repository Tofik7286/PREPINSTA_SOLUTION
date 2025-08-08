# Armstrong number in a given range
low = int(input("Enter Lowest Limit : "))
high = int(input("Enter Highest Limit : "))

for i in range(low, high+1):
    length = len(str(i))
    sum = 0
    original_number = i
    while i != 0:
        r = i % 10
        i = i // 10
        sum += pow(r, length)
    if original_number == sum:
        print(original_number, end=" ")
