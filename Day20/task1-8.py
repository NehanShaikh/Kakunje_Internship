# Simple Line Plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Plot Student Marks
import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
marks = [75,85,60,90,70]

plt.plot(students, marks, marker='o', color='green')
plt.title("Student Marks Line Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


# Bar Chart
import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "CS"]
marks = [80,75,90,85]

plt.bar(subjects, marks)
plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


# Scatter Plot
import matplotlib.pyplot as plt

height = [150,160,165,170,175,180]
weight = [50,55,60,65,70,75]

plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()


# Histogram
import matplotlib.pyplot as plt

marks = [55,60,65,70,75,80,85,90,95,60,70,80]

plt.hist(marks)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()


# Pie Chart
import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [40,25,20,15]

explode = (0.1, 0, 0, 0)

plt.pie(students, labels=languages, explode=explode, shadow=True, autopct='%1.1f%%')
plt.title("Programming Language Preference")
plt.show()


# Customize Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y = x * 2

plt.plot(x, y, marker='o', linestyle='--', color='red')
plt.title("Customized Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Plot Sales Data
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200,300,250,400,350]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
