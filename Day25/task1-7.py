# Task 1 – User Registration Module
print("Welcome to AIML Academy!\n")

full_name = input("Enter Full Name: ")
age = int(input("Enter Age: "))
course_fee = float(input("Enter Course Fee: "))
email = input("Enter Email: ")

first_name = full_name[:full_name.index(" ")]

initials = full_name[0] + "." + full_name[full_name.index(" ") + 1]

email = email.lower()

print("\n\tStudent Registration Details")
print(f"Student Name: {full_name}")
print(f"Initials: {initials}")
print(f"Age: {age}")
print(f"Course Fee: ₹{course_fee:.2f}")
print(f"Email: {email}")


# Task 2 – Sales Data Tracker
sales = []

for i in range(1, 6):
    amount = int(input(f"Enter sale amount {i}: "))
    sales.append(amount)

print("\nDaily Sales:", sales)

total = sum(sales)
average = total / len(sales)

print("Total Revenue:", total)
print("Average Revenue:", average)

ascending = sorted(sales)
descending = sorted(sales, reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)

lowest = min(sales)
sales.remove(lowest)

print("Lowest sale removed:", lowest)
print("Updated Sales List:", sales)

if any(sale < 1000 for sale in sales):
    print("Low Sales Alert Triggered!")


# Task 3 – Employee Skill Management System
employee1 = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "AI",
    "Skills": {"Python", "ML", "SQL"}
}

employee2 = {
    "ID": 102,
    "Name": "Amit",
    "Department": "AI",
    "Skills": {"Python", "SQL", "Deep Learning"}
}

employee1["Skills"].add("NLP")

all_skills = employee1["Skills"].union(employee2["Skills"])
common_skills = employee1["Skills"].intersection(employee2["Skills"])

print("\nAll Skills (Union):", all_skills)
print("Common Skills (Intersection):", common_skills)

salary_grade = ("Grade A", 50000, 70000)

grade, min_salary, max_salary = salary_grade

print("Salary Grade:", grade)
print("Salary Range:", min_salary, "-", max_salary)

print("\nEmployee 1 Details:")
for key, value in employee1.items():
    print(key, ":", value)


# Task 4 – Hospital Management System (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError("Age cannot be negative!")
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def get_details(self):
        print(f"Doctor {self.name}, Specialization: {self.specialization}")

class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__medical_record = "Confidential"

    def get_details(self):
        print(f"Patient {self.name}, Age: {self.age}")

try:
    d1 = Doctor("Dr. Mehta", 45, "Cardiology")
    p1 = Patient("Ravi", 30)

    d1.get_details()
    p1.get_details()

except Exception as e:
    print("Error:", e)


# Task 5 – Mini Data Analysis Project
import numpy as np
import pandas as pd

marks = np.array([85, 90, 78, 90, 85, 88])
marks_2d = marks.reshape(3, 2)

print("\nMini Data Analysis Project")
print("2D Array:\n", marks_2d)

df = pd.DataFrame(marks_2d, columns=["Maths", "Science"])

df.loc[1, "Science"] = np.nan

df["Science"].fillna(df["Science"].mean(), inplace=True)
df.drop_duplicates(inplace=True)

print("\nCleaned DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())


# Task 6 – Color Theme Switcher (Tkinter)
import tkinter as tk

def light_mode():
    root.config(bg="white")
    label.config(bg="white", fg="black")
    entry.config(bg="white", fg="black")

def dark_mode():
    root.config(bg="black")
    label.config(bg="black", fg="white")
    entry.config(bg="gray", fg="white")

def blue_theme():
    root.config(bg="lightblue")
    label.config(bg="lightblue", fg="darkblue")
    entry.config(bg="white", fg="blue")

root = tk.Tk()
root.title("Color Theme Switcher")
root.geometry("300x200")

label = tk.Label(root, text="Enter Name:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Light Mode", command=light_mode).pack(pady=2)
tk.Button(root, text="Dark Mode", command=dark_mode).pack(pady=2)
tk.Button(root, text="Blue Theme", command=blue_theme).pack(pady=2)

root.mainloop()


# Task 7 – Smart Hospital Management Assistant
import datetime
import random
import math
import os
import sys

print("\n--- Smart Hospital Management Assistant ---")

now = datetime.datetime.now()
print("\nCheck-In Time:", now)
print("Day:", now.strftime("%A"))

doctors = ["Dr. Mehta", "Dr. Sharma", "Dr. Rao"]
assigned_doctor = random.choice(doctors)
room = random.randint(100, 500)

print("\nAssigned Doctor:", assigned_doctor)
print("Room Number:", room)

bill = 5000
tax = bill * 0.18
total_bill = bill + tax

print("\nTotal Bill:", bill)
print("Service Tax:", tax)
print("Final Bill (Rounded):", math.ceil(total_bill))

filename = "patient_record.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Patient Record Created\n")
    print("\nNew patient file created.")
else:
    print("\nPatient file already exists.")

print("\nPython Version:", sys.version)
print("System Arguments:", sys.argv)

print("\nSystem exiting safely...")
sys.exit()
