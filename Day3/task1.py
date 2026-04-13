"""
["apple", "banana", "cherry"]
1. ["apple", "banana", "cherry", "orange"]
2. ["apple", "mango", "banana", "cherry", "orange"]
3. ["apple", "mango", "banana", "cherry", "orange", "kiwi", "grape"]
"""

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)

fruits.insert(1, "mango")
print(fruits)

fruits.extend(["kiwi", "grape"])
print(fruits)
