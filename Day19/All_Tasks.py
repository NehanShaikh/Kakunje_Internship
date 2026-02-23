# Task1
text = "Artificial Intelligence"

print(text[:10])

print(text[-5:])

print(text[::2])

print(text[::-1])

print(text[11:])


# Task2
email = "student@gmail.com"

print(email[:7])

print(email[8:13])

print(email[-3:])


# Task3
numbers = [10, 20, 30, 40, 50]

numbers.append(60)
print(numbers)

numbers.remove(30)
print(numbers)

numbers.insert(2, 25)
print(numbers)

maximum = max(numbers)
minimum = min(numbers)
print("Max:", maximum)
print("Min:", minimum)

numbers.reverse()
print(numbers)


# Task4
data = [12, 45, 67, 23, 89, 45, 12, 90]

data = list(set(data))
print(data)

asc = sorted(data)
print("Ascending:", asc)

desc = sorted(data, reverse=True)
print("Descending:", desc)


# Task5
t = (10, 20, 30, 40, 50)

print(t[0])
print(t[-1])

print(len(t))

print(30 in t)

l = list(t)
print(l)


# Task6
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

print(student.keys())

print(student.values())

student["grade"] = "A"
print(student)

student["marks"] = 90
print(student)

student.pop("age")
print(student)


# Task7
def add(a, b):
    return a + b
print("Result:", add(5, 3))


def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("Result:", even_odd(7))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print("Fact:", factorial(5))


# Task8
for i in range(1, 6):
    print(str(i) * i)


# Task9
num = 12345
total = 0

for digit in str(num):
    total = total + int(digit)

print("Result:", total)


# Task10
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


# Task11
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print("First Row:")
print(df.iloc[0])

print("\nMarks Column:")
print(df["Marks"])


# Task12
import pandas as pd

df = pd.read_csv("Students.csv")

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nColumn Names:")
print(df.columns)

df_no_null = df.dropna()
print("\nData after removing null values:")
print(df_no_null)

df_filled = df.fillna(df.mean(numeric_only=True))
print("\nData after replacing null values with mean:")
print(df_filled)
