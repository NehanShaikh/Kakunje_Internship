"""
Matrix A = [[2, 4, 6],
            [8, 0, 1],
            [3, 5, 7]]
Functional updates for Matrix A
1) Add row [10, 11, 12] at last
2) Add column [13, 14, 15] at last
3) Add row [16, 17, 18] at pos1
4) Add column [19, 20, 21] at pos2
"""

A = [
    [2, 4, 6],
    [8, 0, 1],
    [3, 5, 7]
    ]

A.append([10, 11, 12])
print(A)

col = [13, 14, 15, 16]
for i in range(len(A)):
    A[i].append(col[i])
print(A)

A.insert(1, [16, 17, 18, 20])
print(A)

col2 = [19, 20, 21, 22, 23]
for i in range(len(A)):
    A[i].insert(2, col2[i])
print(A)
