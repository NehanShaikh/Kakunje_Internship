import numpy as np

salaries = [25000, 30000, 28000, 32000, 29000, 31000, 27000, 35000, 26000]

# 1. Create 1D array
arr1 = np.array(salaries)
print("1D Array:", arr1)

# 2. Convert to 2D (3x3)
arr2 = arr1.reshape(3,3)
print("2D Array:\n", arr2)

# 3. Shape, dtype, element access
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)
print("Salary at row 2 column 1:", arr2[1,0])

# 4. Slicing
print("Index 2 to 6:", arr1[2:7])
print("Last 3 salaries:", arr1[-3:])

# 5. Sorting
print("Ascending:", np.sort(arr1))
print("Descending:", np.sort(arr1)[::-1])

# 6. Reshape back to 1D
arr_back = arr2.reshape(-1)
print("Reshaped to 1D:", arr_back)

# 7. Join with bonus
bonus = np.array([2000, 3000, 2500, 4000, 1500, 3500, 2800, 5000, 1800])
joined = np.concatenate((arr1, bonus))
print("Joined Array:", joined)
