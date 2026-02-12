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
