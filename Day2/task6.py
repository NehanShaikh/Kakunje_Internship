"""
s = "LogicalThinking"
Write Python code to get the following outputs using string slicing only.
a) Thinking
b) gniknihTlacigoL
c) LglTiki
d) lacigo
e) giTk
Write Python code to:
1) Print the character at index 3
2) Print the character at index -4
3) Print characters from index 2 to index 7
4) Print characters from index -8 to -1
5) Print the string except the first 3 characters
"""

s = "LogicalThinking"

# Thinking
print(s[7::1])
print(s[-8::1])

# gnihkniTlacigoL
print(s[::-1])
print(s[-1:-16:-1])

# LglTiki
print(s[0::2])
print(s[-15::2])

# lacigo
print(s[6:0:-1])
print(s[-9:-15:-1])

# giTk
print(s[2:12:3])
print(s[-13:-3:3])

# Print the character at index 3
print(s[3])

# Print the character at index -4
print(s[-4])

# Print characters from index 2 to index 7
print(s[2:8])

# Print characters from index -8 to -1
print(s[-8:-1])

# Print the string except the first 3 characters
print(s[3:])
print(s[-12:])
