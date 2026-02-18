import numpy as np

stock = np.array([45, 60, 30, 80, 55, 90, 20, 70])

# 1. zeros, ones, arange
print("Zeros:", np.zeros(8))
print("Ones:", np.ones(8))
print("Arange 10-50 step 5:", np.arange(10, 50, 5))

# 2. Convert to 2D (4x2)
stock2d = stock.reshape(4,2)
print("2D Stock:\n", stock2d)

# 3. Access elements
print("Row 3 Column 1:", stock2d[2,0])
print("First Row:", stock2d[0])

# 4. Slicing
print("Index 1 to 5:", stock[1:6])
print("Index -4 to -1:", stock[-4:-1])

# 5. Searching
print("Index where stock is 90:", np.where(stock == 90))
print("Values > 50:", stock[stock > 50])

# 6. Splitting
print("Split into 4 parts:", np.split(stock,4))
print("Vertical Split:", np.vsplit(stock2d,2))
print("Horizontal Split:", np.hsplit(stock2d,2))
