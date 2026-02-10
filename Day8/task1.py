"""
1. Write a function to multiply two numbers and return the result and print it in the function call.
2. Create a function to check whether a number is even or odd.
3. Write a function to find the maximum of three numbers.
4. Create a function to calculate the factorial of a number.
5. Write a function to count vowels in a given string.
6. Define a function to reverse a string.
7. Write a function to check if a number is prime.
8. Write a function using default arguments.
9. Create a function using keyword arguments.
10. Write a recursive function to calculate Fibonacci series.
11.Write a lambda function to find the square of a number
"""

# 1. Function to multiply two numbers and return the result
def multiply(a, b):
    return a * b

print("Multiplication =", multiply(4, 5))

# 2. Function to check whether a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(7))

# 3. Function to find the maximum of three numbers
def maximum(a, b, c):
    return max(a, b, c)

print("Maximum number =", maximum(10, 25, 15))

# 4. Function to calculate the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("Factorial =", factorial(5))

# 5. Function to count vowels in a given string
def count_vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
    return count

print("Vowels count =", count_vowels("Python Programming"))

# 6. Function to reverse a string
def reverse_string(text):
    return text[::-1]

print("Reversed string =", reverse_string("Python"))

# 7. Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(7))

# 8. Function using default arguments
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Adam")

# 9. Function using keyword arguments
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="steve")

# 10. Recursive function to calculate Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci series:")
for i in range(6):
    print(fibonacci(i), end=" ")

# 11. Lambda function to find the square of a number
square = lambda x: x * x

print("Square =", square(6))
