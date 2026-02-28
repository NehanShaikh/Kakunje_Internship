"""
7. Find Maximum in List Without max()
"""

L = [10, 45, 3, 78, 22]

largest = L[0]
for num in L:
    if num > largest:
        largest = num

print("Maximum:", largest)
