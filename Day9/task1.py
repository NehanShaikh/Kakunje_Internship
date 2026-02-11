# Create a class Student
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

s1 = Student("ABC", 101)
s2 = Student("XYZ", 102)

s1.display()
s2.display()
