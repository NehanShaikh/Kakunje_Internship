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
