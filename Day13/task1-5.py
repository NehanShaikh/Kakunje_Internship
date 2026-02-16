# Employee Data
import csv

with open("employee_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Age", "Department"])
    writer.writerow(["Alice", 25, "HR"])
    writer.writerow(["Bob", 30, "Finance"])
    writer.writerow(["Charlie", 28, "IT"])

print("Employee Data Written Successfully!")

print("Reading employee_data.csv...")
with open("employee_data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("employee_dict.csv", mode="w", newline="") as file:
    fieldnames = ["Name", "Age", "Department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 25, "Department": "HR"})
    writer.writerow({"Name": "Bob", "Age": 30, "Department": "Finance"})
    writer.writerow({"Name": "Charlie", "Age": 28, "Department": "IT"})

print("Dictionary CSV file created successfully!")


# Date and Time Record
import datetime

now = datetime.datetime.now()
print("System Date:", now.date())
print("System Time:", now.time())

print("Year :", now.year)
print("Month:", now.month)
print("Day :", now.day)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date & Time:", formatted)


# System Time Tracking
import time

timestamp = time.time()
print("Current Timestamp:", timestamp)
print("Readable Time:", time.ctime())

print("Waiting for 2 seconds...")
time.sleep(2)

print("Continuing execution...")


# Data Backup
import zipfile
import tarfile

print("Creating backup.zip...")
with zipfile.ZipFile("backup.zip", "w") as zipf:
    zipf.write("employee_data.csv")
    zipf.write("employee_dict.csv")

print("Creating backup.tar.gz...")
with tarfile.open("backup.tar.gz", "w:gz") as tar:
    tar.add("employee_data.csv")
    tar.add("employee_dict.csv")

print("Files inside backup.zip:")
with zipfile.ZipFile("backup.zip", "r") as zipf:
    print(zipf.namelist())

print("Files inside backup.tar.gz:")
with tarfile.open("backup.tar.gz", "r:gz") as tar:
    print(tar.getnames())

print("Backup completed successfully!")


# Background Backup
import threading
import time

def background_backup():
    for _ in range(3):
        print("Backup running in background...")
        time.sleep(2)

t = threading.Thread(target=background_backup)
t.start()

print("Main program continues working...")
t.join()

print("Main thread finished!")
print("Program Completed Successfully!")
