import json
import os

# Parent Class
class LibraryItem:
    def __init__(self, title):
        self.title = title


# Child Class
class Book(LibraryItem):
    def __init__(self, title, author, book_id, borrowed=False):
        super().__init__(title)
        self.author = author
        self.book_id = book_id
        self.borrowed = borrowed
    def show_details(self):
        status = "Borrowed" if self.borrowed else "Available"
        print("ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)
        print("-" * 30)

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "borrowed": self.borrowed
        }


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.filename = "books.json"
        self.load_books()

    # Load books from JSON file
    def load_books(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    for book in data:
                        new_book = Book(
                            book["title"],
                            book["author"],
                            book["book_id"],
                            book["borrowed"]
                        )
                        self.books.append(new_book)
        except (json.JSONDecodeError, KeyError):
            print("Error reading books.json. Starting with empty library.")

    # Save books to JSON file
    def save_books(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add new book
    def add_book(self):
        try:
            book_id = input("Enter book ID: ").strip()
            if not book_id:
                raise ValueError("Book ID cannot be empty.")
            for book in self.books:
                if book.book_id == book_id:
                    print("Book ID already exists.")
                    return
            title = input("Enter book title: ").strip()
            if not title:
                raise ValueError("Book title cannot be empty.")
            author = input("Enter author name: ").strip()
            if not author:
                raise ValueError("Author name cannot be empty.")
            new_book = Book(title, author, book_id)
            self.books.append(new_book)
            self.save_books()
            print("Book added successfully!")
        except ValueError as error:
            print("Invalid input:", error)

    # View all books
    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return
        print("\n--- All Books ---")
        for book in self.books:
            book.show_details()

    # Search for a book
    def search_book(self):
        search = input("Enter book title or author: ").lower()
        found = False
        for book in self.books:
            if search in book.title.lower() or search in book.author.lower():
                book.show_details()
                found = True
        if not found:
            print("Book not found.")

    # Borrow a book
    def borrow_book(self):
        book_id = input("Enter book ID to borrow: ")
        for book in self.books:
            if book.book_id == book_id:
                if book.borrowed:
                    print("This book is already borrowed.")
                else:
                    book.borrowed = True
                    self.save_books()
                    print("Book borrowed successfully.")
                return
        print("Book not found.")

    # Return a book
    def return_book(self):
        book_id = input("Enter book ID to return: ")
        for book in self.books:
            if book.book_id == book_id:
                if not book.borrowed:
                    print("This book was not borrowed.")
                else:
                    book.borrowed = False
                    self.save_books()
                    print("Book returned successfully.")
                return
        print("Book not found.")


# Create Library
library = Library()


# Main Menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            library.search_book()

        elif choice == 4:
            library.borrow_book()

        elif choice == 5:
            library.return_book()

        elif choice == 6:
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid input! Please enter a number.")