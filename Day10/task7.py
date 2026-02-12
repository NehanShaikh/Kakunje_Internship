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
