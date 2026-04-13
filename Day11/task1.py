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
