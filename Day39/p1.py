matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

row_sum = []

for row in matrix:
    row_sum.append(sum(row))

print("Row Sum:", row_sum)


col_sum = [0,0,0]

for row in matrix:
    for i in range(len(row)):
        col_sum[i] += row[i]

print("Column Sum:", col_sum)
