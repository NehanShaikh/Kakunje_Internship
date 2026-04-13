# Task 1: Basic Variable Assignment
name = "Nehan"
age = 21
height = 5.6

print(f"My name is {name}, I am {age} years old and my height is {height} feet.")


# Task 2: Multiple Variables
# Assign values to three variables in a single line and print their sum
a, b, c = 5, 10, 15

print(a + b + c)


# Task 3: Using Parentheses (Line Continuation)
# Store the sum of multiple numbers using parentheses
total = (
    10 +
    20 +
    30 +
    40
)

print(total)


# Task 4: String Continuation
# Create a long string message using implicit continuation inside parentheses
n = (
    "Hello! My name is Nehan. "
    "I am learning Python programming. "
    "This message is created using implicit string continuation."
)

print(n)


# Task 5: List Continuation
# Create a list of at least 8 elements written across multiple lines
n = [
    1, 2, 3, 4,
    5, 6, 7, 8
]

print(n)


# Task 6: Simple Input
# Ask the user to enter their name and print a welcome message
name = input("Enter your name: ")

print("Welcome,", name)


# Task 7: Integer Input
# Ask the user to enter two numbers and print sum, difference, and product
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Diff:", num1 - num2)
print("Product:", num1 * num2)


# Task 8: Input, Data Type, and Conversion
# Take two numbers, print their values and data types, then convert and add
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("First value:", num1)
print("Second value:", num2)

print("Data type of first value:", type(num1))
print("Data type of second value:", type(num2))

sum = int(num1) + int(num2)
print("Sum: ", sum)
