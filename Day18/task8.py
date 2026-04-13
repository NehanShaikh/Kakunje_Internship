# Task8
import datetime, math, os

temps = []
for i in range(5):
    t = float(input(f"Enter temp for day {i+1}: "))
    temps.append(t)

avg = math.ceil(sum(temps)/len(temps))
max_t = max(temps)
min_t = min(temps)

if avg >= 35:
    status = "Hot Week"
elif 20 <= avg < 35:
    status = "Pleasant Week"
else:
    status = "Cold Week"

with open("weather_report.txt", "w") as f:
    f.write(f"Average: {avg}\nStatus: {status}")

print("Report Date:", datetime.date.today())
print("Max:", max_t, "Min:", min_t, "Avg:", avg)
