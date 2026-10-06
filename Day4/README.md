# Day 4 – File Handling, JSON & Student Record Management System

## What I Learned

Today I learned:

* File handling in Python
* Reading and writing text files
* Appending data to files
* Counting lines in a file
* JSON in Python
* Reading and writing JSON files
* Using exception handling
* Creating a persistent Student Record Management System

## Student Record Management System

I upgraded my previous Student Record Management System by adding JSON file storage.
The system can:

* Add student records
* View student records
* Search students by roll number
* Update student information
* Delete student records
* Automatically load existing records
* Permanently save changes to a JSON file
* Handle invalid inputs using exception handling

## How File Handling and JSON Work Together

Python file handling is used to open and save the `students.json` file.
JSON stores student information in a structured format. When the program starts, it loads the existing data from the JSON file. Whenever a student is added, updated, or deleted, the changes are saved back to the file.

## Challenges Faced

The main challenge was understanding how to load existing JSON data and save changes permanently. I also practiced using `try-except` to handle invalid inputs and prevent the program from crashing.

## Conclusion

This project helped me understand how Python applications can store, retrieve, update, and manage data permanently using JSON.
