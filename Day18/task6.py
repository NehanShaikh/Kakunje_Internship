# Task6
import datetime, math, os

name = input("Customer Name: ")
city = input("Destination City: ")
travelers = int(input("Number of Travelers: "))
cost = float(input("Cost per Ticket: "))

now = datetime.datetime.now()

total = travelers * cost
final = total + (0.05 * total)
final = math.ceil(final)

filename = "booking.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write(f"Customer: {name}\nCity: {city}\nTotal Cost: {final}")

print("Booking Time:", now)
print("Final Cost:", final)
print("File Created Successfully")
