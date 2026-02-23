"""
Task 4

data = [12, 45, 67, 23, 89, 45, 12, 90]

Remove duplicates
Sort ascending
Sort descending
"""

data = [12, 45, 67, 23, 89, 45, 12, 90]

data = list(set(data))
print(data)

asc = sorted(data)
print("Ascending:", asc)

desc = sorted(data, reverse=True)
print("Descending:", desc)
