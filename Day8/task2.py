"""
1. Handle ZeroDivisionError.
2. Handle ValueError when converting input to integer.
3. Write a program using try and except.
4. Write a program using try, except, else.
5. Write a program using try, except, finally.
6. Handle TypeError.
7. Handle multiple exceptions in a single try block.
8. Raiseanexception using raise keyword
"""

# 1. Handle ZeroDivisionError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# 2. Handle ValueError when converting input to integer
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Please enter a valid integer")

# 3. Program using try and except
try:
    x = int(input("Enter a number: "))
    print("Square =", x * x)
except:
    print("Error occurred")

# 4. Program using try, except, else
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Number entered:", num)
    print("Square =", num * num)

# 5. Program using try, except, finally
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division =", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program execution completed")

# 6. Handle TypeError
try:
    a = 10
    b = "Python"
    print(a + b)
except TypeError:
    print("Error: Cannot add integer and string")

# 7. Handle multiple exceptions in a single try block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result =", result)
except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero")

# 8. Raise an exception using raise keyword
age = int(input("Enter age: "))

if age < 18:
    raise Exception("Age must be 18 or above")
else:
    print("Eligible to vote")
