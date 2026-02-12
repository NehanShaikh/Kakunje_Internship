import math

# 1. Take a number from user
num = float(input("Enter a number: "))

# 2. Print Square Root
print("Square Root:", math.sqrt(num))

# Print Factorial
if num >= 0 and num.is_integer():
    print("Factorial:", math.factorial(int(num)))
else:
    print("Factorial: Not defined for negative or decimal numbers")

# Print Floor value
print("Floor value:", math.floor(num))

# Print Ceiling value
print("Ceiling value:", math.ceil(num))
