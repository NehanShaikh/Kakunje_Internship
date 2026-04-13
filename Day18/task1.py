# Task1
import os

filename = "diary.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Today was productive.\n")
        f.write("Learned Python file handling.\n")
        f.write("Worked on internship tasks.\n")
        f.write("Improved coding skills.\n")
        f.write("Feeling motivated!\n")

with open(filename, "r") as f:
    content = f.read()
    print("\nFull Diary:\n", content)

print("\nFirst 50 characters:\n", content[:50])

print("\nDiary Line by Line:")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())

os.remove(filename)
print("\nDiary file deleted.")
