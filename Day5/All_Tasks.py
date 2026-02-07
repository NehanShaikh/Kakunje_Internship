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


"""
t1 = (1, 2, 3)

7. Multiply the tuple t1 by 3 and print the result.
"""

t1 = (1, 2, 3)

# 7. Multiply the tuple by 3
result = t1 * 3
print(result)


"""
my_set = {10, 20, 30, 40}

1. Print the given set.
2. Check whether 20 is present in my_set.
3. Find and print the length of my_set.
4. Add 50 to my_set.
5. Remove 30 from my_set.
6. Remove an element using discard() and note the output.
7. Remove a random element from my_set.
8. Loop through my_set and print each element.
9. Clear all elements from my_set.
"""
my_set = {10, 20, 30, 40}

# 1. Print the given set
print(my_set)

# 2. Check whether 20 is present in my_set
print(20 in my_set)

# 3. Find and print the length of my_set
print(len(my_set))

# 4. Add 50 to my_set.
my_set.add(50)
print(my_set)

# 5. Remove 30 from my_set.
my_set.remove(30)
print(my_set)

# 6. Remove an element using discard() and note the output.
my_set.discard(20)
print(my_set)

# 7. Remove a random element from my_set.
my_set.pop()
print(my_set)

# 8. Loop through my_set and print each element.
for item in my_set:
    print(item)
    
# 9. Clear all elements from my_set
my_set.clear()
print(my_set)


"""
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

10. Print the elements that are in set1 but not in set2.
11. Print the elements that are in either set1 or set2 but not in both (symmetric difference).
12. Add all items from set2 into set1 and print the updated set1.
13. Print all unique elements from both set1 and set2.
14. Add 7 to set1 and print the set.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# 10. Elements in set1 but not in set2
print(set1 - set2)

# 11. Elements in either set1 or set2 but not in both (symmetric difference)
print(set1 ^ set2)

# 12. Add all items from set2 into set1
set1.update(set2)
print(set1)

# 13. Print all unique elements from both set1 and set2
print(set1 | set2)

# 14. Add 7 to set1
set1.add(7)
print(set1)


"""
Given Dictionary:
    
student = {
"name": "Anu",
"age": 20,
"course": "Python"
}

1. Print all keys, values, and all items in the dictionary.
2. Access the value of "name".
3. Access the value of "course" using get().
4. Add a new key "marks" with value 85.
5. Update the value of "age" to 21.
6. Remove "course" using pop().
7. Remove the last inserted item using popitem().
8. Loop through the dictionary and print keys and values.
"""

student = {
    "name": "Anu",
    "age": 20,
    "course": "Python"
}

# 1. Print all keys, values, and items
print(student.keys())
print(student.values())
print(student.items())

# 2. Access the value of "name"
print(student["name"])

# 3. Access the value of "course" using get()
print(student.get("course"))

# 4. Add a new key "marks" with value 85
student["marks"] = 85
print(student)

# 5. Update the value of "age" to 21
student["age"] = 21
print(student)

# 6. Remove "course" using pop()
student.pop("course")
print(student)

# 7. Remove the last inserted item using popitem()
student.popitem()
print(student)

# 8. Loop through the dictionary and print keys and values
for key, value in student.items():
    print(key, ":", value)


"""
students = {
"student1": {"'name": "Anu", "age": 20},
"student2": {"name": "Ravi", "age": 21}
}

9. Print the complete nested dictionary.
10. Create a copy of the students dictionary.
"""

students = {
    "student1": {"name": "Anu", "age": 20},
    "student2": {"name": "Ravi", "age": 21}
}

# 9. Print the complete nested dictionary
print(students)

# 10. Create a copy of the students dictionary
students_copy = students.copy()
print(students_copy)


"""
employee = {
"emp_id": 101,
"name": "Kiran",
"department": "HR",
"salary": 35000
}

13. Display all keys in the employee dictionary.
14. Display all values in the employee dictionary.
15. Display all key-value pairs (items) from the dictionary.
16. Access and print the value of "name".
17. Update the "salary" to 40000.
"""

employee = {
    "emp_id": 101,
    "name": "Kiran",
    "department": "HR",
    "salary": 35000
}

# 13. Display all keys
print(employee.keys())

# 14. Display all values
print(employee.values())

# 15. Display all key-value pairs
print(employee.items())

# 16. Access and print the value of "name"
print(employee["name"])

# 17. Update the "salary" to 40000
employee["salary"] = 40000
print(employee)
