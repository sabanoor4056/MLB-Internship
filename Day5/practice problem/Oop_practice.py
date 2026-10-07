# =========================
# OOP PRACTICE
# =========================

# 1. Student Class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
student1 = Student("Saba", 22, "IET")
student2 = Student("Ali", 21, "Computer Science")
print("STUDENTS")
student1.show_details()
print()
student2.show_details()


# 2. Employee Class

class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary
    def show_details(self):
        print("Name:", self.name)
        print("Job:", self.job)
        print("Salary:", self.salary)
employee1 = Employee("Ahmed", "Software Developer", 60000)
print("\nEMPLOYEE")
employee1.show_details()


# 3. Car Class

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    def start(self):
        print(self.brand, self.model, "is starting.")
    def stop(self):
        print(self.brand, self.model, "has stopped.")
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
car1 = Car("Toyota", "Corolla", "White")
car2 = Car("Honda", "Civic", "Black")
print("\nCARS")
car1.show_details()
car1.start()
print()
car2.show_details()
car2.start()
car2.stop()


# =========================
# INHERITANCE
# =========================

# 4. Person Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)


# Student inherits from Person

class StudentPerson(Person):
    def introduce(self):
        print("I am", self.name, "and I am a student.")
    def study(self):
        print(self.name, "is studying.")


# Teacher inherits from Person

class Teacher(Person):
    def introduce(self):
        print("I am", self.name, "and I am a teacher.")
    def teach(self):
        print(self.name, "is teaching.")
student = StudentPerson("Saba", 22)
teacher = Teacher("Ahmed", 35)
print("\nINHERITANCE")
student.introduce()
student.study()
print()
teacher.introduce()
teacher.teach()