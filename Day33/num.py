# NUMPY TASKS
import numpy as np

# Task 1
arr = np.arange(1,11)
print(arr)

# Task 2
data = np.array([10,20,30,40,50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))

# Task 3
rand_nums = np.random.rand(10)
print(rand_nums)

# Task 4
a = np.arange(1,7)
reshaped = a.reshape(2,3)
print(reshaped)

# Task 5
print("Max:", np.max(data))
print("Min:", np.min(data))

# Task 6
zeros = np.zeros((3,3))
ones = np.ones((3,3))
print(zeros)
print(ones)
