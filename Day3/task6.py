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
