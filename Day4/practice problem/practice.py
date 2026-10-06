import json

# =========================
# FILE HANDLING PRACTICE
# =========================

# Create and write to a file
with open("practice.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("I am learning JSON\n")
    file.write("my name is saba\n")
    file.write("i am in final year\n")
print("File created successfully.")

# Read the file
with open("practice.txt", "r") as file:
    content = file.read()
print("\nFile Content:")
print(content)

# Append new data
with open("practice.txt", "a") as file:
    file.write("Day 4 Practice\n")
print("New data added.")

# Count lines
with open("practice.txt", "r") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))


# =========================
# JSON PRACTICE
# =========================

student = {
    "name": "Saba",
    "age": 22,
    "course": "Python",
    "uni": "superior university" 
}

# Save dictionary to JSON
with open("practice.json", "w") as file:
    json.dump(student, file, indent=4)
print("\nJSON file created.")

# Read JSON
with open("practice.json", "r") as file:
    data = json.load(file)
print("JSON Data:")
print(data)