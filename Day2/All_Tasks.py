# String Slicing

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


"""
"Python String Slicing Example"
1) gnirtS nohtyP
2) Slicing Example
3) emEni iS oy
4) Potgigae
5) elpmaxE
6) gtoP
"""

s= "Python String Slicing Example"

# gnirtS nohtyP
print(s[12::-1])
print(s[-17::-1])

# Slicing Example
print(s[14::1])
print(s[-15::1])

# emEni iS oy
print(s[28:0:-3])
print(s[-1:-29:-3])

# Potgigae
print(s[0::4])
print(s[-29::4])

# elpmaxE
print(s[28:21:-1])
print(s[-1:-8:-1])

# gtoP
print(s[12::-4])
print(s[-17::-4])


"""
"Python is easy to learn"
1) easy
2) rae
3) es ola
4) si nohtyP
5) tnsa  a
6) nhy
7) easy to learn
8) ot ysae
"""

s= "Python is easy to learn"

# easy
print(s[10:14:1])
print(s[-13:-9:1])

# rae
print(s[21:18:-1])
print(s[-2:-5:-1])

# es ola
print(s[10:21:2])
print(s[-13:-2:2])

# si nohtyP
print(s[8::-1])
print(s[-15::-1])

# tnsa  a
print(s[2:21:3])
print(s[-21:-2:3])

# nhy
print(s[5:0:-2])
print(s[-18:-23:-2])

# easy to learn
print(s[10::1])
print(s[-13::1])

# ot ysae
print(s[16:9:-1])
print(s[-7:-14:-1])


"""
"One of the world's spectacular bridge is Tower Bridge"
1) Tower Bridge
2) world's spectacular
3) egdirb
4) Ooho'paare ere
5) rasleo
"""

s= "One of the world's spectacular bridge is Tower Bridge"

# Tower Bridge
print(s[41::1])
print(s[-12::1])

# world's spectacular
print(s[11:31])
print(s[-42:-22])

# egdirb
print(s[36:29:-1])
print(s[-17:-24:-1])

# Ooho'paare ere
print(s[0::4])
print(s[-53::4])

# rasleo
print(s[29:3:-5])
print(s[-24:-50:-5])


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
