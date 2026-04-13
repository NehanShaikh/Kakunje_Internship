# Task1
s = "Machine Learning"
print(s.upper())
print(s.lower())
print([s[0:5], s[6:12], s[13], s[-1]])

# Task2
s = "Plants need air, water and sunlight to grow"
print(s[12:26])
print(s[15::-1])
print(s[7:35:3])
print(s[::-1])
print(s[2::5])

# Task3
s = "Indentation is very important in Python"
print(s[-11:-21:-1])
print(s[-2:-20:-2])
print(s[13::-1])

# Task4
lst1 = [10,20,30,40,50]
lst1.insert(3,35)
lst1.append(60)
print(lst1)

# Task5
lst2 = ["Lion","Tiger","Elephant","Leopard"]
lst2.insert(1,"Cheetah")
lst2.append("Monkey")
lst2.insert(0,"Giraffe")
print(lst2)

# Task6
t = (1,2,3,4,5)
print(t)
t = tuple(list(t)[:4])
print(t)

# Task7
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(matrix[1])
print(matrix[2], matrix[3])
print([row[0] for row in matrix])
print([matrix[1][2], matrix[1][3]], [matrix[2][2], matrix[2][3]])
print([matrix[i][i] for i in range(4)])
print([matrix[i][3-i] for i in range(4)])

# Task8
matrix2 = [
    [1,2,3,4],
    [3,6,8,9],
    [4,7,9,10]
]
matrix2.append([6,6,6,6])
matrix2.insert(2,[20,25,30,35])
print(matrix2)

# Task9
def check_password(p):
    u=l=n=s=sp=0
    for i in p:
        if i.isupper(): u=1
        elif i.islower(): l=1
        elif i.isdigit(): n=1
        else: sp=1
    score = u+l+n+sp
    if score<=2: return "Weak"
    elif score==3: return "Medium"
    else: return "Strong"

print(check_password("Abc@123"))

# Task10
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, b):
        self.books.append(b)

    def issue_book(self, b):
        if b in self.books:
            self.books.remove(b)
            print("Issued:", b)

    def return_book(self, b):
        self.books.append(b)

    def show_books(self):
        print(self.books)

lib = Library()
lib.add_book("Python")
lib.add_book("AI")
lib.issue_book("Python")
lib.show_books()

# Task11
balance = 1000
pin = "1234"
attempts = 0

while attempts < 3:
    p = input("Enter PIN: ")
    if p == pin:
        while True:
            print("1.Deposit 2.Withdraw 3.Check 4.Exit")
            ch = input("Choice: ")
            if ch == "1":
                amt = int(input("Amount: "))
                balance += amt
            elif ch == "2":
                amt = int(input("Amount: "))
                balance -= amt
            elif ch == "3":
                print("Balance:", balance)
            elif ch == "4":
                break
        break
    else:
        attempts += 1
else:
    print("Account Blocked")

# Task12
import pandas as pd

data = {
    "Name":["A","B","C","D"],
    "Marks":[80,90,70,85],
    "Subject":["Math","Sci","Eng","Math"]
}
df = pd.DataFrame(data)
print(df["Marks"].mean())
print(df.loc[df["Marks"].idxmax()])
print(df[df["Marks"]>75])

# Task13
import matplotlib.pyplot as plt

products = ["A","B","C"]
sales = [100,200,150]
months = [1,2,3]
growth = [10,20,30]

plt.figure()
plt.bar(products, sales)
plt.show()

plt.figure()
plt.plot(months, growth)
plt.show()

plt.figure()
plt.pie(sales, labels=products)
plt.show()

# Task14
import tkinter as tk
import joblib
import pandas as pd

try:
    model = joblib.load("model.pkl")
except:
    print("Model has not been trained")
    model = None

df = pd.read_csv("Iris.csv")

def predict():
    if model is None:
        result.config(text="Model not loaded")
        return
    try:
        values = [
            float(e1.get()),
            float(e2.get()),
            float(e3.get()),
            float(e4.get())
        ]
        prediction = model.predict([values])[0]
        result.config(text=f"Prediction: {prediction}")
    except:
        result.config(text="Invalid Input")

root = tk.Tk()
root.title("Iris Prediction App")
root.geometry("350x300")

tk.Label(root, text="Enter Iris Features", font=("Arial", 14))\
    .grid(row=0, column=0, columnspan=2, pady=10)

labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entries.append(entry)

e1, e2, e3, e4 = entries

tk.Button(root, text="Predict", command=predict)\
    .grid(row=5, column=0, columnspan=2, pady=15)

result = tk.Label(root, text="", font=("Arial", 12))
result.grid(row=6, column=0, columnspan=2)

root.mainloop()

# Task15
class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, price):
        self.items[name] = price

    def remove(self, name):
        self.items.pop(name, None)

    def total(self):
        return sum(self.items.values())

    def display(self):
        print(self.items)

c = Cart()
c.add("Pen",10)
c.add("Book",50)
c.remove("Pen")
c.display()
print("Total:", c.total())

# Task16
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg = self.average()
        if avg>=90: return "A"
        elif avg>=75: return "B"
        else: return "C"

s = Student("Ali",[80,90,70])
print(s.total(), s.average(), s.grade())
