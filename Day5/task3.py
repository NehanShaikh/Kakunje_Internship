"""
my_set = {10, 20, 30, 40}

1. Print the given set.
2. Check whether 20 is present in my_set.
3. Find and print the length of my_set.
4. Add 50 to my_set.
5. Remove 30 from my_set.
6. Remove an element using discard() and note the output.
7. Remove a random element from my_set.
8. Loop through my_set and print each element.
9. Clear all elements from my_set.
"""
my_set = {10, 20, 30, 40}

# 1. Print the given set
print(my_set)

# 2. Check whether 20 is present in my_set
print(20 in my_set)

# 3. Find and print the length of my_set
print(len(my_set))

# 4. Add 50 to my_set.
my_set.add(50)
print(my_set)

# 5. Remove 30 from my_set.
my_set.remove(30)
print(my_set)

# 6. Remove an element using discard() and note the output.
my_set.discard(20)
print(my_set)

# 7. Remove a random element from my_set.
my_set.pop()
print(my_set)

# 8. Loop through my_set and print each element.
for item in my_set:
    print(item)
    
# 9. Clear all elements from my_set
my_set.clear()
print(my_set)
