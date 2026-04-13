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
