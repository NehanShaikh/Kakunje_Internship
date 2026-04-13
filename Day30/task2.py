# Task 2 - Check whether two strings are anagrams

str1 = "listen"
str2 = "silent"

if sorted(str1.lower()) == sorted(str2.lower()):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
