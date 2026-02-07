"""
B = [ 
[9, 8, 7], 
[1, 3, 2], 
[4, 6, 5] 
]

[8,7] [3, 2]
[4,6]
[9,3,5]
[7,3,4]
Add column [1, 1, 1] after column [7,2,5]
[8,1] [3,1] [6,1]
[1,1]
Add row [0,0,0,0] after [1, 3,2,1]
Add column [ 10, 10, 10, 10] after [8,3,6,0]
[8,7] [6,5]
"""

B = [ 
    [9, 8, 7], 
    [1, 3, 2], 
    [4, 6, 5] 
]

# 1) [8,7] [3,2]
print(B[0][1:], B[1][1:])

# 2) [4,6]
print(B[2][:2])

# 3) [9,3,5]
print([B[i][i] for i in range(len(B))])

# 4) [7,3,4]
print([B[i][2-i] for i in range(len(B))])

# 5) Add column [1, 1, 1] after column [7,2,5]
for i in range(len(B)):
    B[i].insert(3, 1)
print(B)

# 6) [8,1] [3,1] [6,1]
print([[B[i][1], B[i][3]] for i in range(len(B))])

# 7) [1,1]
print([B[1][0], B[1][3]])

# 8) Add row [0,0,0,0] after [1,3,2,1]
B.insert(2, [0, 0, 0, 0])
print(B)

# 9) Add column [10, 10, 10, 10] after [8,3,6,0]
for i in range(len(B)):
    B[i].insert(2, 10)
print(B)

# 10) [8,7] [6,5]
print([B[0][1], B[0][3]], [B[3][1], B[3][3]])
