"""
Operators Task

1. Calculate the sum, difference, product, and quotient of two numbers.
2. Find the remainder of a division.
3. Calculate simple interest.
4. Convert minutes to hours and minutes.
5. Find the square and cube of a number.
6. Check if a student has passed (marks ≥ 40).
7. Compare two ages and print who is older.
8. Check if a number is greater than or equal to 100.
9. Check if a number is positive OR zero.
10.Check if a number is NOT negative.
"""

# 1. Calculate the sum, difference, product, and quotient of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)

# 2. Find the remainder of a division.
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
print("Remainder =", a % b)

# 3. Calculate simple interest.
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)

# 4. Convert minutes to hours and minutes.
minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print("Hours =", hours)
print("Minutes =", remaining_minutes)

# 5. Find the square and cube of a number.
n = int(input("Enter a number: "))
print("Square =", n ** 2)
print("Cube =", n ** 3)

# 6. Check if a student has passed (marks ≥ 40).
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Student has passed")
else:
    print("Student has failed")

# 7. Compare two ages and print who is older.
age1 = int(input("Enter first age: "))
age2 = int(input("Enter second age: "))
if age1 > age2:
    print("First person is older")
elif age2 > age1:
    print("Second person is older")
else:
    print("Both are of the same age")

# 8. Check if a number is greater than or equal to 100.
num = int(input("Enter a number: "))
if num >= 100:
    print("Number is greater than or equal to 100")
else:
    print("Number is less than 100")

# 9. Check if a number is positive OR zero.
num = int(input("Enter a number: "))
if num > 0 or num == 0:
    print("Number is positive or zero")
else:
    print("Number is negative")

# 10.Check if a number is NOT negative.
num = int(input("Enter a number: "))

if not(num < 0):
    print("Number is not negative")
else:
    print("Number is negative")
