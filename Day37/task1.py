# Task 1 - Print the matrix
matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 8]
]

print("Matrix:")
for row in matrix:
    print(row)

print(matrix[1][2], matrix[0][2])

matrix[2][0] = 700
for row in matrix:
    print(row)

total = 0
for row in matrix:
    for element in row:
        total += element

print(total)

print(matrix[1][0], matrix[1][2], matrix[2][1])
