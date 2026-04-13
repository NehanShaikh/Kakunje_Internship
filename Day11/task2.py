# Create and write into a file
file = open("message.txt", "w")
file.write("Hello, this is my first file handling program.")
file.close()
print("File created and message written successfully.")

# Open file in read mode
file = open("message.txt", "r")
content = file.read()
print("File Content:")
print(content)
file.close()

# Open file in append mode
file = open("message.txt", "a")
file.write("\nThis line is appended to the file.")
file.close()
print("Data appended successfully.")

# Read file line by line
file = open("message.txt", "r")

print("Reading file line by line:")
for line in file:
    print(line.strip())
file.close()
