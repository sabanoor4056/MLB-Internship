import json
FILE_NAME = "students.json"

# Load students from JSON file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON file is empty or incorrect.")
        return []

# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    print("\n--- Add Student ---")
    try:
        roll_number = int(input("Enter Roll Number: "))
        # Check duplicate roll number
        for student in students:
            if student["roll_number"] == roll_number:
                print("Roll number already exists.")
                return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        student = {
            "roll_number": roll_number,
            "name": name,
            "age": age,
            "course": course
        }
        students.append(student)
        save_students(students)
        print("Student added successfully.")
    except ValueError:
        print("Invalid input! Roll number and age must be numbers.")


# View students
def view_students(students):
    print("\n--- Student Records ---")
    if len(students) == 0:
        print("No student records found.")
        return
    for student in students:
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("----------------------")


# Search student
def search_student(students):
    print("\n--- Search Student ---")
    try:
        roll_number = int(input("Enter Roll Number: "))
        for student in students:
            if student["roll_number"] == roll_number:
                print("\nStudent Found!")
                print("Roll Number:", student["roll_number"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input! Roll number must be a number.")

# Update student
def update_student(students):
    print("\n--- Update Student ---")
    try:
        roll_number = int(input("Enter Roll Number: "))
        for student in students:
            if student["roll_number"] == roll_number:
                student["name"] = input("Enter New Name: ")
                student["age"] = int(input("Enter New Age: "))
                student["course"] = input("Enter New Course: ")
                save_students(students)
                print("Student updated successfully.")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input! Age must be a number.")


# Delete student
def delete_student(students):
    print("\n--- Delete Student ---")
    try:
        roll_number = int(input("Enter Roll Number: "))
        for student in students:
            if student["roll_number"] == roll_number:
                students.remove(student)
                save_students(students)
                print("Student deleted successfully.")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input! Roll number must be a number.")


# =========================
# MAIN PROGRAM
# =========================

students = load_students()
print("Student Record Management System")
print("Records loaded successfully.")
while True:

    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice! Please select 1-6.")