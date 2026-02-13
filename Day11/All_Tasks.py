# Coffee Shop Bill System
from abc import ABC, abstractmethod
import os

class BillSystem(ABC):

    @abstractmethod
    def create_bill(self):
        pass

    @abstractmethod
    def add_item(self):
        pass

    @abstractmethod
    def show_bill(self):
        pass

    @abstractmethod
    def cancel_order(self):
        pass

class CoffeeShop(BillSystem):

    def __init__(self):
        self.filename = ""

    def create_bill(self):
        name = input("Enter Customer Name: ")
        self.filename = name + ".txt"

        with open(self.filename, "w") as file:
            file.write("Coffee Shop Bill\n")
            file.write("Customer: " + name + "\n")

        print("Bill Created Successfully")

    def add_item(self):
        item = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))
        price = int(input("Enter Price per item: "))

        total = quantity * price

        with open(self.filename, "a") as file:
            file.write(f"{item} - {quantity} cups - {total}\n")

        print("Item Added Successfully")

    def show_bill(self):
        with open(self.filename, "r") as file:
            print(file.read())

    def cancel_order(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("Order Cancelled")
            print("Bill Deleted Successfully")
        else:
            print("No bill found.")

shop = CoffeeShop()

shop.create_bill()
shop.add_item()
shop.add_item()
shop.show_bill()
shop.cancel_order()


# Create and write into a file
file = open("message.txt", "w")
file.write("Hello, this is my first file handling program.")
file.close()
print("File created and message written successfully.")

# Open file in read mode
file = open("message.txt", "r")
content = file.read()
print("File Content:")
print(content)
file.close()

# Open file in append mode
file = open("message.txt", "a")
file.write("\nThis line is appended to the file.")
file.close()
print("Data appended successfully.")

# Read file line by line
file = open("message.txt", "r")

print("Reading file line by line:")
for line in file:
    print(line.strip())
file.close()


# Method Overriding
class Shape:
    def area(self):
        print("Area of shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)

r = Rectangle(5, 4)
r.area()

# Movie Info
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def check_rating(self):
        if self.rating >= 8:
            print(self.title, "is a Hit Movie")
        else:
            print(self.title, "is an Average Movie")

m1 = Movie("Inception", 9)
m1.check_rating()

# Book Discount
class BookStore:
    def __init__(self, book_name, price):
        self.book_name = book_name
        self.price = price

    def discount(self):
        if self.price > 500:
            discount_price = self.price * 0.9
            print("Discounted Price:", discount_price)
        else:
            print("No Discount Applied")

b1 = BookStore("Python Guide", 600)
b1.discount()

# Password Protection
class UserAccount:
    def __init__(self):
        self.__password = ""

    def set_password(self, pwd):
        if len(pwd) > 6:
            self.__password = pwd
            print("Password Set Successfully")
        else:
            print("Password must be more than 6 characters")

    def validate_password(self, pwd):
        if pwd == self.__password:
            print("Password Matched")
        else:
            print("Incorrect Password")

u = UserAccount()
u.set_password("mypassword")
u.validate_password("mypassword")

# Temperature Control
class Thermostat:
    def __init__(self):
        self.__temperature = 20

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
            print("Temperature Set to", temp)
        else:
            print("Temperature must be between 16 and 30")

    def get_temperature(self):
        return self.__temperature

t = Thermostat()
t.set_temperature(25)
print("Current Temperature:", t.get_temperature())

# Electronics Store
class ElectronicItem:
    def __init__(self, brand):
        self.brand = brand

class WashingMachine(ElectronicItem):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def display(self):
        print("Brand:", self.brand)
        print("Capacity:", self.capacity)

wm = WashingMachine("LG", "7kg")
wm.display()

# Media Player
class AudioPlayer:
    def play_audio(self):
        print("Playing Audio")

class VideoPlayer:
    def play_video(self):
        print("Playing Video")

class SmartPlayer(AudioPlayer, VideoPlayer):
    pass

sp = SmartPlayer()
sp.play_audio()
sp.play_video()
