# Task2
mobile = input("Enter Mobile Number: ")
budget = int(input("Enter Budget: "))

if budget == 199:
    print("Plan: 28 Days Validity")
elif budget == 299:
    print("Plan: 56 Days Validity")
elif budget == 499:
    print("Plan: 84 Days Validity")
else:
    print("No recommended plan available.")
