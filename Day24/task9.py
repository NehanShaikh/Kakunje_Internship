"""
9. Count Uppercase, Lowercase, Digits
"""

text = "Python123ABC"

upper = lower = digit = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
