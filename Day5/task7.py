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
