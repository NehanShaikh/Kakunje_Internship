"""
[42,3.14,"Hello",True]
1. [2.718,3.14,"Hello",True]
2. [2.718,3.14,"Hello",True,1000]
3. [2.718,False,3.14,"Hello",True,1000]
4. [5,3.14,"Hello",True,1000]
"""

lst = [42, 3.14, "Hello", True]

lst[0] = 2.718
print(lst)

lst.append(1000)
print(lst)

lst.insert(1, False)
print(lst)

lst[0] = 5
del lst[1]
print(lst)
