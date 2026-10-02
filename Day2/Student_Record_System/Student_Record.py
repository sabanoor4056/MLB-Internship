# Student Record Management System

# This list will store all student records
students = []

# 1. Add Student

def add_student():

    print("--- Add Student ---")

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    # Taking marks of 3 subjects
    subject1 = float(input("Enter marks for Python: "))
    subject2 = float(input("Enter marks for Database: "))
    subject3 = float(input("Enter marks for AI: "))

    # Calculate average
    average = (subject1 + subject2 + subject3)/3 

    # Assign grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    # Create student dictionary
    student = {
        "name": name,
        "roll_number": roll_number,
        "age": age,
        "course": course,
        "python": subject1,
        "database": subject2,
        "ai": subject3,
        "average": average,
        "grade": grade
    }

    # Add dictionary to students list
    students.append(student)

    print("Student added successfully!")
    print("Average:", round(average, 2))
    print("Grade:", grade)

# 2. View All Students


def view_students():

    print("--- All Students ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:

        print("Name:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])

# 3. Search Student

def search_student():

    print("--- Search Student ---")

    roll_number = input("Enter roll number: ")

    found = False

    for student in students:

        if student["roll_number"] == roll_number:

            print("Student Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])

            found = True
            break

    if found == False:
        print("Student not found.")


# 4. Update Student

def update_student():

    print("--- Update Student ---")

    roll_number = input("Enter roll number of student: ")

    for student in students:

        if student["roll_number"] == roll_number:

            print("Student found!")

            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_course = input("Enter new course: ")

            student["name"] = new_name
            student["age"] = new_age
            student["course"] = new_course

            print("Student information updated successfully!")

            return

    print("Student not found.")

# 5. Delete Student


def delete_student():

    print("--- Delete Student ---")

    roll_number = input("Enter roll number: ")

    for student in students:

        if student["roll_number"] == roll_number:

            students.remove(student)

            print("Student deleted successfully!")

            return

    print("Student not found.")



# 6. Total Number of Students


def total_students():

    print("Total number of students:", len(students))


# 7. Main Menu


while True:

    print("================================")
    print("   STUDENT RECORD SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Number of Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_student()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        total_students()

    elif choice == "7":

        print("Thank you for using Student Record System!")
        break

    else:

        print("Invalid choice. Please try again.")