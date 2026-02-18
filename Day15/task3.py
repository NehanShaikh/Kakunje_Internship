import numpy as np

temperature = np.array([30, 32, 31, 29, 35, 36, 33, 34, 28, 27, 26, 25])

# 1. 1D array
print("1D Array:", temperature)

# 2. Convert to 3D (2x2x3)
temp3d = temperature.reshape(2,2,3)
print("3D Array:\n", temp3d)

# 3. Access element
print("First block, second row, third column:",
      temp3d[0,1,2])

# 4. Data type
print("Data Type:", temperature.dtype)
temperature_float = temperature.astype(float)
print("Changed to Float:", temperature_float.dtype)

# 5. Slicing
print("Index 3 to 8:", temperature[3:9])
print("Every second value:", temperature[::2])

# 6. Sorting
print("Ascending:", np.sort(temperature))
print("Descending:", np.sort(temperature)[::-1])

# 7. Reshape into 4x3
temp4x3 = temperature.reshape(4,3)
print("Reshaped 4x3:\n", temp4x3)
