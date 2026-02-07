"""
Matrix A= [
            [1, 1, 1],
             1, 1, 1],
             1, 1, 1]
]
Add col [0,0,0] last
Add col [5,5,5] pos 1
Add row [1, 2, 3. 4, 5] last
Add row [6, 7, 8, 9, 10] pos 2
Add col [10, 20, 30, 40, 50] last
"""

A = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

col1 = [0, 0, 0]
for i in range(len(A)):
    A[i].append(col1[i])
print(A)

col2 = [5, 5, 5]
for i in range(len(A)):
    A[i].insert(1, col2[i])
print(A)

A.append([1, 2, 3, 4, 5])
print(A)

A.insert(2, [6, 7, 8, 9, 10])
print(A)

col3 = [10, 20, 30, 40, 50]
for i in range(len(A)):
    A[i].append(col3[i])
print(A)
