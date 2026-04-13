# Task7
import datetime, sys, os

name = input("Patient Name: ")
age = int(input("Age: "))
temp = float(input("Body Temperature: "))
heart = int(input("Heart Rate: "))

status = "Fever Detected" if temp > 37.5 else "Normal"

filename = "health_report.txt"

with open(filename, "w") as f:
    f.write(f"Patient: {name}\nStatus: {status}")

print("Checkup Time:", datetime.datetime.now())
print("Python Version:", sys.version)
print("Report Generated Successfully")
