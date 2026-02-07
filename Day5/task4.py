"""
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

10. Print the elements that are in set1 but not in set2.
11. Print the elements that are in either set1 or set2 but not in both (symmetric difference).
12. Add all items from set2 into set1 and print the updated set1.
13. Print all unique elements from both set1 and set2.
14. Add 7 to set1 and print the set.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# 10. Elements in set1 but not in set2
print(set1 - set2)

# 11. Elements in either set1 or set2 but not in both (symmetric difference)
print(set1 ^ set2)

# 12. Add all items from set2 into set1
set1.update(set2)
print(set1)

# 13. Print all unique elements from both set1 and set2
print(set1 | set2)

# 14. Add 7 to set1
set1.add(7)
print(set1)
