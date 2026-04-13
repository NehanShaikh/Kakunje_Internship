# Task 11 - Longest Substring Without Repeating Characters

s = "abcabcbb"

longest = 0

for i in range(len(s)):
    seen = set()
    length = 0
    
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        length += 1
    
    if length > longest:
        longest = length

print("Length of longest substring:", longest)


# Task 12 - First Non-Repeating Character

s = "aabbcdde"

for char in s:
    if s.count(char) == 1:
        print("First non-repeating character:", char)
        break
