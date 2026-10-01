# Python Fundamentals - Day 1
# MLB Internship

# 1. Variables and Data Types
name = "Saba"
age = 22
height = 5.4
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# 2. List
skills = ["Python", "Django", "AI", "Machine Learning"]
print("\nSkills:", skills)
skills.append("GitHub")
print("Updated Skills:", skills)

# 3. Tuple
courses = ("Python", "AI", "Data Annotation")
print("\nCourses:", courses)

# 4. Set
classes = {"Bike", "Car", "Bike", "Person"}
print("\nClasses:", classes)

# 5. Dictionary
student = {
    "name": "Saba",
    "degree": "BS IET",
    "semester": "Final Year"
}
print("\nStudent Information:", student)

# 6. Operators
a = 10
b = 5

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 7. Conditional Statement
marks = 75

if marks >= 50:
    print("\nResult: Pass")
else:
    print("\nResult: Fail")

# 8. Function
def greet(name):
    return "Hello, " + name

message = greet("Saba")
print("\nFunction Output:", message)