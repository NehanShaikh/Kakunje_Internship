"""
Task 7

Write function to:

Add two numbers
Check even or odd
Find factorial
"""

def add(a, b):
    return a + b
print("Result:", add(5, 3))


def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("Result:", even_odd(7))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print("Fact:", factorial(5))
