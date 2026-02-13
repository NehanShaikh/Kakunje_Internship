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
