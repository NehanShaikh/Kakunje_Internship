import statistics

# 1. Create a list of student marks
marks = [78, 85, 92, 88, 76]

# 2. Calculate the average (mean)
average = statistics.mean(marks)

# 3. Calculate the median
median = statistics.median(marks)

# 4. Calculate the standard deviation
std_dev = statistics.stdev(marks)

# 5. Display all calculated results clearly
print("Student Marks:", marks)
print("Average Marks:", average)
print("Median Marks:", median)
print("Standard Deviation:", std_dev)
