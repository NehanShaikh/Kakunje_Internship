# Task10
import datetime, random, math, os, sys

now = datetime.datetime.now()
print("Date:", now.date())
print("Time:", now.strftime("%I:%M %p"))
print("Day:", now.strftime("%A"))

roads = ["Road A", "Road B", "Road C"]
green = random.choice(roads)
duration = random.randint(30, 90)
print("\nTraffic Update:")
print("Green Signal →", green)
print("Duration →", duration, "seconds")

units = [120.5, 130.2, 125.3, 136.8]
total = sum(units)
avg = math.ceil(total/len(units))
print("\nEnergy Report:")
print("Total Units Used:", total)
print("Average Units:", avg)

file = "complaints.txt"
exists = os.path.exists(file)
print("\nComplaint File Exists:", "Yes" if exists else "No")

print("\nPython Version:", sys.version)
print("System Report Generated Successfully!")
