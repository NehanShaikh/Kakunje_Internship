"""
Task 9

Find sum of digits:
num = 12345
"""

num = 12345
total = 0

for digit in str(num):
    total = total + int(digit)

print("Result:", total)
