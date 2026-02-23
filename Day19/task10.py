"""
Task 10

Create class:
student

Attributes:
name, age, marks

Methods:
display()
"""

class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

s1 = Student("ABC", 21, 85)
s1.display()


"""
Create class:
BankAccount

Attributes:
account number
balance

Methods:
deposit ()
withdraw()
display_balance ()
"""

class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

acc1 = BankAccount(12345, 1000)

acc1.deposit(500)
acc1.withdraw(300)
acc1.display_balance()
