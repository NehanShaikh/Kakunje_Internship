# Task1

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Task 2
rows = 4

for i in range(rows):
    
    for j in range(rows - i - 1):
        print(" ", end=" ")
    
    for k in range(2 * i + 1):
        print("*", end=" ")
    
    print()


# Task3
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()


# Task4
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Task5
n = 5

for i in range(n):
    
    for j in range(n - i - 1):
        print(" ", end="")
    
    for k in range(2 * i + 1):
        print("*", end="")
    
    print()

for i in range(n-2, -1, -1):
    
    for j in range(n - i - 1):
        print(" ", end="")
    
    for k in range(2 * i + 1):
        print("*", end="")
    
    print()


# Task6
n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# Task7
n = 5

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


# Task8
n = 5

for i in range(n):
    
    print(" "*(n-i), end="")
    
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num*(i-j)//(j+1)
    
    print()


# Task9
n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")

    print()


# Task10
n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end=" ")
    print()
