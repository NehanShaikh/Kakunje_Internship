# Task 3 - Sum of first N natural numbers

n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum: ",sum)
