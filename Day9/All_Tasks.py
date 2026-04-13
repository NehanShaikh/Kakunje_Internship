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


# Create a class Employee
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

emp1 = Employee(1, "Steve", 50000)
emp1.display()


# Create class College
class College:
    college_name = "Sahyadri College"

    def __init__(self, student_name, branch):
        self.student_name = student_name
        self.branch = branch

    def display(self):
        print("College:", College.college_name)
        print("Student:", self.student_name)
        print("Branch:", self.branch)


c1 = College("ABC", "CSE")
c2 = College("XYZ", "ECE")

c1.display()
c2.display()


# Create class BankAccount
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()


# Single Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

s = Student("Thomas", 20, 85)
s.display()


# Multilevel Inheritance
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def drive(self):
        print("Car is Driving")

class ElectricCar(Car):
    def charge(self):
        print("Car is Charging")

e = ElectricCar()
e.start()
e.drive()
e.charge()


# Mobile Phone
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile("Samsung", 20000)
m2 = Mobile("Apple", 70000)
m3 = Mobile("OnePlus", 30000)

m1.show_details()
m2.show_details()
m3.show_details()


# Laptop Configuration
class Laptop:
    def __init__(self, ram, processor, storage):
        self.ram = ram
        self.processor = processor
        self.storage = storage

    def display(self):
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print("Storage:", self.storage)

l1 = Laptop("16GB", "Intel i5", "512GB SSD")
l1.display()


class Employee:
    
    company_name = "Kakunje Software Pvt Ltd"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Company Name:", Employee.company_name)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("ABC", 50000)
emp2 = Employee("XYZ", 60000)

emp1.display()
emp2.display()
