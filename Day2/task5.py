"""
S = "DATASTRUCTURESANALYSIS"
1. Print the first and last character using index values.
2. Print the character at index 7.
3. Print the character at index -5.
4. Print characters from index 4 to 13.
5. Print the string without the first 4 characters.
6. Print every second character starting from index 0.
7. Print characters at even index positions only.
8. Print the entire string in reverse order.
9. Print characters from index 15 to index 5 in reverse.
10. Print the middle 6 characters using indexing.
"""

s = "DATASTRUCTURESANALYSIS"

# Print the first and last character using index values.
print(s[0], s[21])
print(s[-22], s[-1])

# 2.Print the character at index 7.
print(s[7])
print(s[-15])

# Print the character at index -5.
print(s[-5])

# Print characters from index 4 to 13.
print(s[4:14:1])

# Print the string without the first 4 characters.
print(s[4::1])
print(s[-18::1])

# Print every second character starting from index 0.
print(s[0::2])

# Print characters at even index positions only.
print(s[::2])
print(s[-22::2])

# Print the entire string in reverse order.
print(s[::-1])
print(s[-1:-23:-1])

# Print characters from index 15 to index 5 in reverse.
print(s[15:4:-1])

# Print the middle 6 characters using indexing.
print(s[8:14:1])
print(s[-14:-8:1])
