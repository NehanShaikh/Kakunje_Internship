"""
[1,2,3]
1. [1,100,2,3]
2. [1,100,2,999]
"""

lst = [1, 2, 3]

lst.insert(1, 100)
print(lst)

lst.append(999)
print(lst)
