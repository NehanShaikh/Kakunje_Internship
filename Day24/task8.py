"""
8. Check Palindrome String (Without [ ::- 1])
"""

text = "madam"

reverse = ""
for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
