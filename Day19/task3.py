"""
Task 3:

numbers = [10, 20, 30, 40, 50]

Add 60 to list
Remove 30
Insert 25 at index 2
Find max and min
Reverse list
"""

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
print(numbers)

numbers.remove(30)
print(numbers)

numbers.insert(2, 25)
print(numbers)

maximum = max(numbers)
minimum = min(numbers)
print("Max:", maximum)
print("Min:", minimum)

numbers.reverse()
print(numbers)
