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
