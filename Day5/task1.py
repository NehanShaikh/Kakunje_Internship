"""
Given Tuples:
t1 =(10, 20, "Python", "Code")
t2 = ("A", "B")

1. Access and print the first element of t1.
2. Access and print the last element of t2.
3. Convert t1 into a list, change "Code" to "Program", and convert it back into a tuple.
4. Unpack all elements of t1 into separate variables and print them.
5. Join t1 and t2 and store the result in a new tuple.
6. Access elements from index 1 to 3 of the joined tuple.
"""

t1 = (10, 20, "Python", "Code")
t2 = ("A", "B")

print(t1[0])

print(t2[-1])

l = list(t1)
l[-1] = "Program"
t1 = tuple(l)
print(t1)

a, b, c, d = t1
print(a, b, c, d)

t = t1 + t2
print(t)

print(t[1:4])
