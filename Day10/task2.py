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
