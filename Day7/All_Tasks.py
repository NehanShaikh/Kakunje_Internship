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


"""
Conditional Statements

1. Find the smallest of two numbers.
2. Check if a person is eligible to vote.
3. Check if a number is even or odd.
4. Grade a student based on marks:
o ≥90:A
≥75: B
≥50: C
Else: Fail

Loop Tasks (For)
1. Print numbers from 1 to 10.
2. Print even numbers from 1 to 50.
3. Print multiplication table of a number.
4. Print characters of a string one by one.
5. Calculate the sum of first N numbers.
6. Count vowels in a string.
"""
# 1. Find the smallest of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Smallest number is", a)
else:
    print("Smallest number is", b)

# 2. Check if a person is eligible to vote.
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 3. Check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 4. Grade a student based on marks.
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 1. Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 3. Print multiplication table of a number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 4. Print characters of a string one by one.
text = input("Enter a string: ")
for ch in text:
    print(ch)

# 5. Calculate the sum of first N numbers.
n = int(input("Enter N: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum =", sum)

# 6. Count vowels in a string.
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
print("Number of vowels =", count)


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
