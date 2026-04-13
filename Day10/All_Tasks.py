import os
import sys

# 1. Create a folder named "Intern_Data"
folder_name = "Intern_Data"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully.")
else:
    print("Folder already exists.")

# 2. Inside that folder, create a file named "info.txt"
file_path = os.path.join(folder_name, "info.txt")

# 3. Write your Name and Course inside the file
with open(file_path, "w") as file:
    file.write("Name: Nehan Shaikh\n")
    file.write("Course: B.E CSE (AI & ML)\n")
print("File created and data written successfully.")

# 4. Check whether the file exists or not
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")

# 5. Display the current working directory
print("Current Working Directory:", os.getcwd())

# 6. List all files inside the "Intern_Data" folder
print("Files inside Intern_Data folder:")
print(os.listdir(folder_name))

# 7. Display the operating system type
print("Operating System:", os.name)

# 8. Rename the file from info.txt to student_info.txt
new_file_path = os.path.join(folder_name, "student_info.txt")
os.rename(file_path, new_file_path)
print("File renamed successfully.")


import sys

# 1. Print the script name using sys.argv
print("Script Name:", sys.argv[0])

# 2. Print all command-line arguments entered
print("Command-line Arguments:")
for arg in sys.argv[1:]:
    print(arg)

# 3. Print the Python version
print("Python Version:", sys.version)

# 4. Take user input using standard input
name = sys.stdin.readline().strip()

# 5. Display a welcome message using the entered name
message = "Welcome, " + name + "!"

# 6. Display output using standard output
sys.stdout.write(message + "\n")


import shutil
import os

# 1. Copy a file named "sample.txt"
source_file = "sample.txt"
destination_file = "copy_sample.txt"

# Check if source file exists
if os.path.exists(source_file):
    
    # 2. Paste it as "copy_sample.txt"
    shutil.copy(source_file, destination_file)
    print("File copied successfully.")

    # 3. Print disk usage
    total, used, free = shutil.disk_usage(os.getcwd())
    
    print("Disk Usage Information:")
    print("Total:", total // (1024**3), "GB")
    print("Used:", used // (1024**3), "GB")
    print("Free:", free // (1024**3), "GB")

else:
    print("Source file does not exist.")


import math

# 1. Take a number from user
num = float(input("Enter a number: "))

# 2. Print Square Root
print("Square Root:", math.sqrt(num))

# Print Factorial
if num >= 0 and num.is_integer():
    print("Factorial:", math.factorial(int(num)))
else:
    print("Factorial: Not defined for negative or decimal numbers")

# Print Floor value
print("Floor value:", math.floor(num))

# Print Ceiling value
print("Ceiling value:", math.ceil(num))


import random

# 1. Generate a random number between 1 and 6 (dice roll)
dice = random.randint(1, 6)

# 2. Print the dice result
print("Dice Result:", dice)

# 3. Create a list of cards
cards = ["Ace", "King", "Queen", "Jack"]

# 4. Shuffle the cards randomly
random.shuffle(cards)
print("Shuffled Cards:", cards)

# 5. Generate and print one random card from the shuffled list
random_card = random.choice(cards)
print("Random Card:", random_card)


import statistics

# 1. Create a list of student marks
marks = [78, 85, 92, 88, 76]

# 2. Calculate the average (mean)
average = statistics.mean(marks)

# 3. Calculate the median
median = statistics.median(marks)

# 4. Calculate the standard deviation
std_dev = statistics.stdev(marks)

# 5. Display all calculated results clearly
print("Student Marks:", marks)
print("Average Marks:", average)
print("Median Marks:", median)
print("Standard Deviation:", std_dev)


import json

# 1. Take location and college name as input from the user
location = input("Enter your location: ")
college = input("Enter your college name: ")

# Store data in dictionary format
data = {
    "Location": location,
    "College": college
}

# 2. Store the data in a JSON file named data.json
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data stored successfully in data.json")

# 3. Read the data from the JSON file
with open("data.json", "r") as file:
    stored_data = json.load(file)

# 4. Print the stored data clearly
print("\nStored Data:")
print("Location:", stored_data["Location"])
print("College:", stored_data["College"])
