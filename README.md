#  Library Management System

## Project Description

Library Management System is a desktop-based Python application developed using Tkinter and JSON file storage.

The project demonstrates Object-Oriented Programming (OOP), modular programming, decorators, generators, exception handling, file handling, and unit testing in a practical application.

The system allows users to:
- add books
- search books
- borrow books
- return books
- delete books
- save data permanently

The application is lightweight, simple to use, and does not require external libraries.



# Project Structure

```text
Library_Management_System/

├── data/
│   └── books.json
│
├── tests/
│   └── test_library.py
│
├── book.py
├── library.py
├── file_manager.py
├── main.py
├── README.md
└── report.docx
```

---

# OOP Principles

## Encapsulation

The project uses `Book` and `Library` classes to encapsulate data and operations.

### Book class stores:
- title
- author
- year
- status

### Library class manages:
- adding books
- deleting books
- borrowing books
- returning books
- searching books

---

## Abstraction

The user interacts only with the graphical interface without accessing internal implementation details.

Main operations are abstracted through methods:
- `add_book()`
- `delete_book()`
- `borrow_book()`
- `return_book()`
- `search_book()`

---

## Modular Programming

The project is separated into multiple modules for better readability and maintainability.

| File              | Purpose                  |
|-------------------|--------------------------|
| `main.py`         | GUI and user interaction |
| `library.py`      | Main business logic      |
| `book.py`         | Book model               |
| `file_manager.py` | JSON file operations     |
| `test_library.py` | Unit testing             |

---

# Advanced Python Features

## Decorators

A custom decorator `log_action` is used to log library actions before and after execution.

Example:

```python
@log_action
def add_book(self, book):
    self.books.append(book)
```

---

## Generators

A generator is used to iterate through available books efficiently.

Example:

```python
def available_books_generator(self):
    for book in self.books:
        if book.status == "Available":
            yield book
```

---

## Exception Handling

Exception handling is used for safer file operations and user input validation.

Example:

```python
except FileNotFoundError:
    return []
```

The program handles:
- invalid input
- duplicate books
- missing files
- incorrect year format
- unavailable books

---

# GUI Design

The graphical user interface was created using Tkinter.

The interface includes:
- input fields
- buttons
- listbox
- scrollbar
- message boxes
- dynamic updates

Available operations:
- Add Book
- Search Book
- Delete Book
- Borrow Book
- Return Book

The interface is simple, user-friendly, and easy to navigate.


# File Handling

The application stores all book data in a JSON file.

File used:

```
books.json
```

The system automatically:
- saves books
- loads books
- updates book status
- preserves data after closing the program

Example JSON format:

```json
[
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": "1925",
        "status": "Available"
    }
]
```


#  Functionalities

## Add Book

Adds a new book to the library.

---

## Search Book

Searches books by title using case-insensitive search.

---

## Delete Book

Deletes the selected book after confirmation.

---

## Borrow Book

Changes book status:

```
Available → Borrowed
```

---

## Return Book

Changes status:

```
Borrowed → Available
```

---

## Duplicate Protection

The system prevents duplicate books from being added.



# Architecture Overview

```
GUI (Tkinter)
       ↓
Library Logic
       ↓
File Manager
       ↓
JSON Storage
```


Testing

Unit tests were created using the `unittest` module.

Tested functions:
- `add_book()`
- `delete_book()`
- `borrow_book()`
- `return_book()`



Screen output:



<img width="425" height="353" alt="image" src="https://github.com/user-attachments/assets/a0cec33a-5f13-4b38-a684-74cc917bb01a" />





# Demonstration

## GUI Window

<img width="1092" height="837" alt="image" src="https://github.com/user-attachments/assets/dadeb81c-9ebb-4ee5-af70-08c5f0483933" />

## Adding Books

<img width="1071" height="839" alt="image" src="https://github.com/user-attachments/assets/2375e0d5-4abd-4636-857e-039e6eda4e08" />


## Searching Books

<img width="1092" height="848" alt="image" src="https://github.com/user-attachments/assets/e8ac2075-e7b2-4c7d-a2e7-8e51ec61701f" />


## Borrowing and Returning Books

<img width="444" height="34" alt="image" src="https://github.com/user-attachments/assets/ad89a4e0-98e7-4df9-b78b-c690e07ac7b7" />

<img width="435" height="32" alt="image" src="https://github.com/user-attachments/assets/776677a9-1de9-4e7b-b484-6c5ce9ffb6a3" />


## JSON Storage

<img width="440" height="910" alt="image" src="https://github.com/user-attachments/assets/c23477be-3a6a-4e20-aaaa-ad736a083590" />

# Learning Outcomes

This project helped improve understanding of:
- Object-Oriented Programming
- modular architecture
- GUI development with Tkinter
- decorators
- generators
- JSON handling
- exception handling
- unit testing
- file handling

---

# Challenges

Main challenges during development:
- handling JSON correctly
- synchronizing GUI updates
- organizing project modules
- configuring Tkinter widgets
- validating user input


#  Future Improvements

Possible future features:
- SQLite database
- dark mode
- ISBN support
- categories and genres
- export to Excel/PDF
- multi-user system
- due dates for borrowed books


# Project Value

This project demonstrates:
- GUI development
- Object-Oriented Programming
- modular design
- decorators
- generators
- file handling
- testing
- exception handling

The system is simple, maintainable, scalable, and easy to extend in future versions.



#  Conclusion

Library Management System is a practical desktop application for managing books in a digital library environment.

The project successfully combines GUI development, Object-Oriented Programming, modular programming, and file handling into one complete system.

The application is fully functional, easy to use, and demonstrates important Python development concepts in practice.
