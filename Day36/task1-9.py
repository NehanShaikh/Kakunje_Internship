# Task1
import tkinter as tk

def convert():
    c = float(entry.get())
    f = (c * 9/5) + 32
    result.config(text=f"Fahrenheit: {f}")

root = tk.Tk()
root.title("Temperature Converter")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root,text="Convert",command=convert)
btn.pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()


# Task2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nums = np.random.randint(1,100,20)
df = pd.DataFrame(nums,columns=["Numbers"])

print("Mean:",np.mean(nums))
print("Median:",np.median(nums))
print("Std Dev:",np.std(nums))

plt.hist(nums)
plt.title("Random Number Histogram")
plt.show()


# Task3
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.title,self.author,self.price)

b1 = Book("Python","Guido",500)
b1.display()


# Task4
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cart:
    def __init__(self):
        self.items=[]

    def add(self,product):
        self.items.append(product)

    def total(self):
        t=0
        for i in self.items:
            t+=i.price
        print("Total:",t)

p1=Product("Laptop",50000)
p2=Product("Mouse",500)

cart=Cart()
cart.add(p1)
cart.add(p2)
cart.total()


# Task5
class ATM:
    def __init__(self,balance):
        self.balance=balance

    def check(self):
        print("Balance:",self.balance)

    def deposit(self,amt):
        self.balance+=amt

    def withdraw(self,amt):
        self.balance-=amt

atm=ATM(1000)
atm.deposit(500)
atm.withdraw(200)
atm.check()


# Task6
class Student:
    def __init__(self,name):
        self.name=name

class Teacher:
    def __init__(self,name):
        self.name=name

class Course:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher

    def display(self):
        print(self.name,self.teacher.name)

t=Teacher("Mr Rao")
c=Course("Python",t)
c.display()


# Task7
for num in range(1,101):
    prime=True
    if num>1:
        for i in range(2,num):
            if num%i==0:
                prime=False
                break
        if prime:
            print(num)


# Task8
s="ABCDEFGHIJKL" 
 
print("String :",s) 
print() 
print(s[2:9:2]) 
print(s[-2:-10:-1]) 
print(s[-2:-12:-1]) 
print(s[-2:-9:-2]) 
print(s[::4]) 
print() 


s="Python String Slicing Example" 
print("String :",s) 
print() 
print(s[12::-1])      
print(s[14:])         
print(s[-1::-3])      
print(s[0::4])      
print(s[-1:-8:-1])         
print(s[12::-4])     
print() 
 
 
 
# Task 9
l=["Cat","Dog","Lion","Tiger","Rabbit","Monkey"] 
print("List :",l) 
print() 
print(l[2]) 
print(l[-1],l[-2]) 
print(l[3:0:-1]) 
print(l[:4:3]) 
print(l[3::-3]) 
print(l[-1:-5:-3]) 
print(l[-2::-2]) 
print(l[::-1]) 
print() 
 

l=["apple","banana","cherry"] 
print("List :",l) 
print() 
l.append("orange") 
print(l) 
 
l.insert(3,"cherry") 
print(l) 
 
l.extend(["kiwi","grape"]) 
print(l) 
print() 
 
 
l=[10,20,30,40,50] 
print("List :",l) 
print() 
l[2]=300 
print(l) 
 
l[1],l[2],l[3]=200,3000,400 
print(l) 
print() 
 
l=[1,2,3] 
print("List :",l) 
print() 
l.insert(1,100) 
print(l) 
 
l[-1]=999 
print(l) 
print() 
 
l=[10,20,30,40,50] 
 
print("List :",l) 
print() 
l.append(60) 
print(l) 
 
l.insert(0,5) 
print(l) 
 
l.extend([70,80,90]) 
print(l) 
print() 
 
l=[42,3.14,"Hello",True] 
print("List :",l) 
print() 
 
l[0]=2.718 
print(l) 
 
l.append(True) 
print(l) 
 
l.insert(1,False) 
print(l) 
 
l[0]=5 
l.pop(1) 
print(l) 
print() 
 
s="Hello World, Welcome to Python!" 
print("String :",s) 
print() 
 
print(s.upper()) 
print(s.lower()) 
print(s.split(" ")) 
print(s.split("o")) 
print(s.replace("W","X"))
