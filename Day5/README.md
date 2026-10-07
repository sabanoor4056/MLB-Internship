# Day 5 – OOP and Library Management System

## Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming approach where programs are designed using classes and objects.

In this task, I practiced:

* Classes and objects
* Attributes and methods
* Constructors
* Inheritance
* Method overriding
* Exception handling
* JSON file handling

## Library Management System

I created a console-based Library Management System using Python and OOP.

The system allows the user to:

* Add a new book
* View all books
* Search for a book
* Borrow a book
* Return a book
* Exit the program

Book records are stored in a JSON file so the data remains saved after the program is closed.

## Inheritance

Inheritance was used through the `LibraryItem` and `Book` classes.

`LibraryItem` is the parent class, while `Book` is the child class.

This allows the Book class to reuse attributes and functionality from the parent class.

## Exception Handling

Exception handling was used to handle invalid user input, such as entering text when the program expects a number.

## Challenges and Solutions

One challenge was understanding how to connect classes with JSON file storage. I solved this by converting book objects into dictionaries before saving them to the JSON file.

Another challenge was handling invalid input. I used `try-except` blocks to prevent the program from crashing.

## Conclusion

This project helped me understand how OOP concepts can be used to build a structured and reusable Python application.
