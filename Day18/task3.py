# Task3
cloth_type = input("Enter type (Cotton/Wool/Synthetic): ")
num = int(input("Enter number of clothes: "))
weight = float(input("Enter weight per cloth (kg): "))

total = num * weight

if total <= 7:
    status = "Wash Started"
else:
    status = "Overload! Reduce clothes"

print("\nCloth Type:", cloth_type)
print("Total Load:", total, "kg")
print("Status:", status)
