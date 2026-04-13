# Task4
class BusTicket:
    def __init__(self, name, bus_no, seat):
        self.name = name
        self.bus_no = bus_no
        self.seat = seat

    def display(self):
        print(f"Passenger: {self.name}, Bus: {self.bus_no}, Seat: {self.seat}")

t1 = BusTicket("Asha", "KA01", 12)
t2 = BusTicket("Ravi", "KA02", 15)

t1.display()
t2.display()
