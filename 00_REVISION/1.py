# Positive or Negative number:
# 1. Brute Force 

num = int(input("Enter Number :"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Naegative")
else:
    print("Zero")


print("Zero" if num == 0 else("Positive" if num > 0 else "Negative"))