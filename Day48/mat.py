# MATPLOTLIB TASKS
import matplotlib.pyplot as plt

# Task 1
months = ["Jan","Feb","Mar","Apr","May"]
sales = [100,150,200,180,220]
plt.plot(months,sales)
plt.title("Monthly Sales")
plt.show()

# Task 2
students = ["A","B","C","D"]
marks = [80,90,70,85]
plt.bar(students,marks)
plt.title("Student Marks")
plt.show()

# Task 3
height = [150,160,170,180]
weight = [50,60,65,75]
plt.scatter(height,weight)
plt.title("Height vs Weight")
plt.show()

# Task 4
ages = [18,20,22,22,23,25,27,30]
plt.hist(ages)
plt.title("Age Distribution")
plt.show()

# Task 5
plt.plot(months,sales,label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Task 6
sales2 = [90,120,160,170,200]
plt.plot(months,sales,label="2024")
plt.plot(months,sales2,label="2025")
plt.legend()
plt.show()

# Task 7
plt.plot(months,sales,color="red",marker="o")
plt.grid(True)
plt.show()
