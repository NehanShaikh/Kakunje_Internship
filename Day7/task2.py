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
