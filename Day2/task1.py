"""
"ABCDEFGHIJKL"
1) CEGI
2) KJIHGFED
3) KJIHGFEDCB
4) KIGE
5) AEI
"""

s= "ABCDEFGHIJKL"

# CEGI
print(s[2:9:2])
print(s[-10:-3:2])

# KJIHGFED
print(s[10:2:-1])
print(s[-2:-10:-1])

# KJIHGFEDCB
print(s[10:0:-1])
print(s[-2:-12:-1])

# KIGE
print(s[10:3:-2])
print(s[-2:-9:-2])

# AEI
print(s[0:9:4])
print(s[-12:-3:4])
