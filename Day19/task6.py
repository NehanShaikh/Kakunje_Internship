"""
Task 6

student f {
"name": "Rahul",
"age": 21,
"marks": 85
}

Print all keys
Print all values
Add new key "grade"
Update marks
Remove age
"""

student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

print(student.keys())

print(student.values())

student["grade"] = "A"
print(student)

student["marks"] = 90
print(student)

student.pop("age")
print(student)
