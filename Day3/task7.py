"""
l1=[50, "apple", True, "car", 40.5]
1) Find length of l1
2) replace True with False
3) [50, "kiwi", "boat", 20, "car", 40.5]
4) [5000, "kiwi", "boat", 20, "car", 40.5]
5) ["kiwi", "boat", 20, "car", 40.5] using remove()
6) ["kiwi", 20, "car", 40.5] using pop()
7) ["kiwi", 20, "car"] using del
8) ["kiwi", 20, "car", 100]
9) ["banana", "kiwi", 20, "car", 100]
10) ["banana", "kiwi", 20, 30.5, "car", 100]
11) []
"""

l1 = [50, "apple", True, "car", 40.5]

print(len(l1))

l1[2] = False
print(l1)

l1[1:3] = ["kiwi", "boat", 20]
print(l1)

l1[0] = 5000
print(l1)

l1.remove(5000)
print(l1)

l1.pop(1)
print(l1)

del l1[-1]
print(l1)

l1.append(100)
print(l1)

l1.insert(0, "banana")
print(l1)

l1.insert(3, 30.5)
print(l1)

l1.clear()
print(l1)
