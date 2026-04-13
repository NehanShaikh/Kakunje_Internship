# Sequence Type list

"""
["apple", "banana", "cherry"]
1. ["apple", "banana", "cherry", "orange"]
2. ["apple", "mango", "banana", "cherry", "orange"]
3. ["apple", "mango", "banana", "cherry", "orange", "kiwi", "grape"]
"""

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)

fruits.insert(1, "mango")
print(fruits)

fruits.extend(["kiwi", "grape"])
print(fruits)


"""
[10,20,30,40,50]
1. [10,20,300,40,50]
2. [10,200,3000,400,50]
"""

nums = [10, 20, 30, 40, 50]

nums[2] = 300
print(nums)

nums[1:4] = [200, 3000, 400]
print(nums)


"""
[1,2,3]
1. [1,100,2,3]
2. [1,100,2,999]
"""

lst = [1, 2, 3]

lst.insert(1, 100)
print(lst)

lst.append(999)
print(lst)


"""
[10,20,30,40,50]
1. [10,20,30,40,50,60]
2. [5,10,20,30,40,50,60]
3. [5,10,20,30,40,50,60,70,80,90]
"""

lst = [10, 20, 30, 40, 50]

lst.append(60)
print(lst)

lst.insert(0, 5)
print(lst)

lst.extend([70, 80, 90])
print(lst)


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


"""
["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]
1) ["lion"]
2) ["Monkey", "Rabbit"]
3) ["Tiger", "Lion", "Dog"]
4) ["Cat", "Tiger"]
5) ["Tiger", "Cat"]
6) ["Monkey", "Lion"]
7) ["Rabbit", "Lion", "Cat"]
8) ["Monkey", "Rabbit", "Tiger", "Lion", "Dog", "Cat"]
"""

animals = ["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]

print(animals[2:3])

print(animals[-1:-3:-1])

print(animals[3:0:-1])

print(animals[::3])

print(animals[3::-3])

print(animals[-1:-5:-3])

print(animals[4::-2])

print(animals[::-1])


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


"""
l2=[50, -1, 2, 100, -6, -3, 67, 79, -55]
1) reverse the list
2) sort in ascending order
3) sort in descending order
"""

l2 = [50, -1, 2, 100, -6, -3, 67, 79, -55]

l2.reverse()
print(l2)

l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)
