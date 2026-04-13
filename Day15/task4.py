import numpy as np

roll_numbers = np.arange(101,111)
print("Roll Numbers:", roll_numbers)

# Zeros & Ones
print("Zeros:", np.zeros(10))
print("Ones:", np.ones(10))

# Convert to 2D (5x2)
roll2d = roll_numbers.reshape(5,2)
print("2D Roll Numbers:\n", roll2d)

# Join with extra roll numbers
extra_roll = np.array([111,112,113,114,115])
joined_roll = np.concatenate((roll_numbers, extra_roll))
print("Joined Roll Numbers:", joined_roll)

# Search
print("Index of 105:", np.where(joined_roll == 105))
print("Roll numbers > 107:", joined_roll[joined_roll > 107])

# Split into 3 equal parts
split_roll = np.split(joined_roll,3)
print("Split into 3 parts:", split_roll)

# Shape check
print("Shape before reshape:", joined_roll.shape)
reshaped = joined_roll.reshape(3,5)
print("Shape after reshape:", reshaped.shape)
