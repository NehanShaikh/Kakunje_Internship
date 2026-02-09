"""
Loop Tasks (While)
1. Print numbers from 10 to 1.
2. Sum of digits of a number.
3. Count number of digits.
"""

# 1. Print numbers from 10 to 1.
i = 10
while i >= 1:
    print(i)
    i = i - 1

# 2. Sum of digits of a number.
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)

# 3. Count number of digits.
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count = count + 1
    num = num // 10

print("Number of digits =", count)
