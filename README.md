# Library Management System

A Python-based library management system that allows users to borrow and return books, track borrowing history, and manage library inventory.

## Project Description

This application provides a simple command-line interface for managing a library system. Users can:
- View available books in the library
- Borrow books (with duplicate borrowing prevention)
- Return borrowed books
- Track their borrowing history with timestamps
- Persist data to JSON files

The system includes data validation, error handling, and automated transaction logging.

## Features

- **Book Management**: Track book availability and borrowing status
- **User Management**: Maintain user profiles and borrowing history
- **Transaction Logging**: Automatic timestamp logging for all transactions
- **Data Persistence**: Save and load library state from JSON files
- **Error Handling**: Comprehensive validation and error messages

## Project Structure

```
.
├── main.py                    # CLI application entry point
├── data/                      # JSON data files
│   ├── books.json
│   └── users.json
├── models/                    # Data models
│   ├── book.py
│   ├── person.py
│   ├── user.py
│   └── __init__.py
├── services/                  # Business logic
│   ├── library_service.py
│   └── __init__.py
├── utils/                     # Utility functions
│   ├── files_handler.py       # JSON file I/O
│   └── __init__.py
└── tests/                     # Unit tests
    ├── test_models.py
    ├── test_services.py
    ├── test_library.py
    └── __init__.py
```


## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ITP2-Final-Library
   ```

2. **Verify Python installation**:
   ```bash
   python --version
   ```

## Running the Application

From the project root, run:

```bash
python main.py
```

The CLI will present a menu with the following options:
1. View Available Books
2. Borrow a Book
3. Return a Book
4. View User History
5. Exit

## Running Tests

Execute all unit tests:

```bash
python -m unittest discover -s tests
```

Run specific test file:

```bash
python -m unittest tests.test_models
python -m unittest tests.test_services
python -m unittest tests.test_library
```

## Usage Example

```
Library Menu
1. View Available Books
2. View all Books
3. View all Users 
4. Find Books by Author
5. Borrow a Book
6. Return a Book
7. View User History
0. Exit

Select an option (1-5): 1
[1] Python by Guido van Rossum - Available
[2] Clean Code by Robert Martin - Borrowed

Select an option (1-5): 2
Enter user ID: 10
Enter book ID: 1
Borrowed successfully.
```

## Team Members

| Name | Role |
|------|------|
| Olzhas | JSON handling, Optimization for O(1) lookups |
| Miras | OOP, Polymorphism, Inheritance, Encapsulation |
| Amirlan | Python features, library_service.py |
| Mansur | Unit testing, decorator, main.py |
