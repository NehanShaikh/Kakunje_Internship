# Task1
s = "Python Programming Language"
 
print(s[7:18]) 
print(s[::-1]) 
print(s[1::2]) 
print(s[-1:-11:-1])

# Task2
s = "Artificial Intelligence"
print(s[11:])
print(s[:10][::-1])
print(s[:10][::-1] + " " + s[11:][::-1])

# Task3
lst = [5, 15, 25, 35, 45]
lst.insert(3, 30)
lst.remove(15)
lst.append(50)
lst[2] = 100
print(lst)

# Task4
lst = ["Apple", "Banana", "Cherry"]
lst.insert(0, "Mango")
lst.insert(2, "Orange")
lst.remove("Apple")
lst.sort()
print(lst)

# Task5
matrix = [
    [2,4,6],
    [8,10,12],
    [14,16,18]
]
print([row[0] for row in matrix])
print([matrix[i][i] for i in range(3)])
print(matrix[-1])

# Task6
matrix = [
    [1,2,3],
    [4,5,6]
]
matrix.append([7,8,9])
matrix.insert(0,[0,0,0])
print(matrix)

# Task7
import json

data = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60}
]

with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json","r") as f:
    d = json.load(f)

topper = max(d, key=lambda x: x["marks"])
print(topper)

d.append({"name":"C","marks":90})

with open("data.json","w") as f:
    json.dump(d,f)

# Task8
def check_email(e):
    if "@" in e and (e.endswith(".com") or e.endswith(".in")):
        return True
    return False

print(check_email("test@gmail.com"))

# Task9
import random
num = random.randint(1,100)

for i in range(5):
    guess = int(input("Enter number: "))
    if guess == num:
        print("Correct")
        break
    elif guess > num:
        print("Too High")
    else:
        print("Too Low")

# Task10
def primes(n):
    res = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            res.append(i)
    print(res)
    print(len(res))
    print(max(res))

primes(50)

# Task11
contacts = {}

def add(name, num):
    contacts[name] = num

def search(name):
    print(contacts.get(name,"Not Found"))

def delete(name):
    contacts.pop(name,None)

def display():
    print(contacts)

add("Ali",123)
add("Sara",456)
search("Ali")
delete("Sara")
display()

# Task12
import cv2

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200)
resized = cv2.resize(img,(200,200))

cv2.imshow("Gray",gray)
cv2.imshow("Edges",edges)
cv2.imshow("Resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task13
import threading

def numbers():
    for i in range(5):
        print(i)

def alphabets():
    for i in "ABCDE":
        print(i)

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=alphabets)

t1.start()
t2.start()

# Task14
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
import joblib 
import tkinter as tk 
 
df=pd.read_csv("iris.csv") 
 
x=df.drop(columns=["Id","Species"]) 
y=df["Species"] 
 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) 
 
model=DecisionTreeClassifier() 
model.fit(x_train,y_train) 
 
joblib.dump(model,"model.pkl") 
print("Model trained and saved") 
 
def predict(): 
    vals=[float(e1.get()), 
          float(e2.get()), 
          float(e3.get()), 
          float(e4.get()) 
          ] 
    res=model.predict([vals]) 
    result.config(text=res) 
 
root=tk.Tk() 
root.title("Prediction App") 
root.geometry("300x350") 
 
heading=tk.Label(root,text="Iris Prediction",font=("Arial",14)) 
heading.pack(pady=10) 
 
tk.Label(root,text="Sepal length").pack() 
e1=tk.Entry(root) 
e1.pack(pady=5) 
 
tk.Label(root,text="Sepal width").pack() 
e2=tk.Entry(root) 
e2.pack(pady=5) 
 
tk.Label(root,text="Petal length").pack() 
e3=tk.Entry(root) 
e3.pack(pady=5) 
 
tk.Label(root,text="Petal width").pack() 
e4=tk.Entry(root) 
e4.pack(pady=5) 
 
tk.Button(root,text="Predict",command=predict).pack(pady=10) 
 
result=tk.Label(root,text="") 
result.pack(pady=10) 
 
root.mainloop() 
 
print()

# Task15
 
import librosa as lb 
import matplotlib.pyplot as plt 
import librosa.display 
 
y,sr=lb.load("D:\\Internship\\Day21\\game_over.wav",sr=None) 
 
print("Sampling Rate:",sr) 
 
plt.figure(figsize=(10,4)) 
lb.display.waveshow(y,sr=sr) 
 
plt.title("Waveform") 
plt.xlabel("Time")
plt.ylabel("Amplitude") 
 
plt.show()

# Task16

import cv2 
import numpy as np 
 
img=cv2.imread("image.jpg") 
 
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
print("Grayscale applied") 
 
blur=cv2.GaussianBlur(img,(7,7),0) 
print("Blur applied") 
 
kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) 
sharp=cv2.filter2D(img,-1,kernel) 
print("Sharpen applied") 
 
cv2.imshow("Original",img) 
cv2.imshow("Gray",gray) 
cv2.imshow("Blur",blur) 
cv2.imshow("Sharpen",sharp) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Task17
class Employee:
    def __init__(self,n,i,s):
        self.name=n
        self.id=i
        self.salary=s

    def inc(self,amt):
        self.salary+=amt

    def display(self):
        print(self.name,self.id,self.salary)

    def annual(self):
        print(self.salary*12)

e = Employee("Ali",1,20000)
e.inc(5000)
e.display()
e.annual()

# Task18 & 19
class Vehicle:
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

v = Car("Car",100)
print(v.name,v.rate)

# Task20
class Patient:
    def __init__(self,name):
        self.name=name

class Doctor:
    def __init__(self,name):
        self.name=name

class Appointment:
    def __init__(self,p,d):
        self.p=p
        self.d=d

a = Appointment("Ali","Dr.X")
print(a.p,a.d)

# Task21
class Order:
    def __init__(self):
        self.items=[]

    def add(self,item,price):
        self.items.append(price)

    def total(self):
        return sum(self.items)

o = Order()
o.add("Burger",100)
o.add("Pizza",200)
print(o.total())
