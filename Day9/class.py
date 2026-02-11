class Student:
    def __init__(self, name, age) :
        self.Name = name
        self.Age = age

    def info (self) :
        print (f"Name: {self.Name} ")
        print (f"Age: {self.Age}")

s1 = Student ("Alice", 20)
s2 = Student ("John", 15)

s1.info()
s2.info()
