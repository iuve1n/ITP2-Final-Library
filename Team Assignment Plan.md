# Library Management System
## Team Assignment Plan

A structured breakdown of responsibilities for building the Library Management System as a team project.

---

## General Rules for Everyone

- Comment your code to explain non-obvious logic.
- Use meaningful variable and function names.
- Commit and push to GitHub regularly so each member's contribution is visible.

---

## Student 1 - Data and Utility Engineer (File Handling)

**Goal:** Ensure the system can safely read from JSON files and save updates permanently.

### Files to Create and Manage

- `data/books.json`
- `data/users.json`
- `utils/file_handler.py`

### Functions to Implement in `utils/file_handler.py`

- [ ] `load_data(filepath)`
  - Read a JSON file.
  - Include `try...except` error handling so the app does not crash if the file is missing.
- [ ] `save_data(filepath, data)`
  - Write updated dictionaries back to JSON.
- [ ] `initialize_system()`
  - Load both JSON files.
  - Convert loaded lists into dictionaries.

### Important Rule

Convert data into dictionaries using IDs as keys, for example:

```python
{1: BookObject, 2: BookObject}
```

This enables fast $O(1)$ lookups instead of repeated list scans.

---

## Student 2 - Object-Oriented Architect (Classes)

**Goal:** Build OOP blueprints demonstrating Encapsulation, Inheritance, and Polymorphism.

### Files to Create and Manage

- `models/book.py`
- `models/person.py`

### Minimum Classes to Implement

#### 1) `Book`

**Properties**

- `book_id` (`int`)
- `title` (`str`)
- `author` (`str`)
- `__is_available` (`bool`) - private attribute (Encapsulation)

**Methods**

- [ ] `__init__(self, book_id, title, author, available)`
- [ ] `get_availability(self)`
- [ ] `set_availability(self, status)`
- [ ] `__str__(self)`

#### 2) `Person` (Base Class)

**Properties**

- `user_id` (`int`)
- `name` (`str`)

**Methods**

- [ ] `__init__(self, user_id, name)`
- [ ] `get_role(self)` - base method to be overridden (Polymorphism)

#### 3) `User` (Inherits from `Person`)

**Properties**

- Inherits `user_id`, `name`
- `active_borrowed_books` (`set`) - prevents duplicate active borrows
- `borrow_history` (`list[tuple]`) - stores past books with dates

**Methods**

- [ ] `__init__(self, user_id, name, borrowed_books_list)`
  - Convert loaded JSON list into a `set`.
- [ ] `get_role(self)` -> returns `"Library User"`
- [ ] `add_book(self, book_id)`
- [ ] `remove_book(self, book_id)`

---

## Student 3 - Logic Master (Services and Advanced Features)

**Goal:** Implement library rules with efficient logic and advanced Python features.

### Files to Create and Manage

- `services/library_service.py`

### Functions and Features to Implement

#### Borrow Logic

- [ ] `borrow_book(user_id, book_id, users_dict, books_dict)`
  - Rule 1: Validate that the book exists and is available.
  - Rule 2: Check whether the user already has that book in `active_borrowed_books`.
  - Rule 3: Set book status to `False` and add book ID to the user's active set.

#### Return Logic

- [ ] `return_book(user_id, book_id, users_dict, books_dict)`
  - Rule 1: Remove from user's active set and set book status to `True`.
  - Rule 2: Add a tuple entry to user's `borrow_history`.

#### Advanced Feature 1 - Generator

- [ ] `yield_available_books(books_dict)`
  - Use `yield` to iterate through `books_dict` and return only books where `get_availability() == True`.

#### Advanced Feature 2 - Lambda and Filter

- [ ] `get_user_history(user_id)`
  - Use `filter()` and `lambda` to retrieve a specific user's history efficiently.

---

## Student 4 - Director (Main Menu, Decorators and Testing)

**Goal:** Integrate all modules, add a decorator, and verify functionality with tests.

### Files to Create and Manage

- `main.py`
- `tests/test_library.py`
- `README.md`

### Tasks to Implement

#### Advanced Feature 3 - Decorator

- [ ] Create `@log_transaction` in `main.py`.
- [ ] Apply it above the `borrow_book` call.
- [ ] Print transaction time, for example:

```text
Transaction occurred at 10:15 AM
```

#### Main Program Loop

- [ ] Build a `while True` menu in `main.py`:
  1. View Available Books
  2. Borrow a Book
  3. Return a Book
  4. View User History
  5. Exit

#### Unit Testing

- [ ] Use Python `unittest` for Student 3 logic.
- [ ] Add a success test for `borrow_book`.
- [ ] Add an edge case test where borrowing an already borrowed book fails correctly.

#### README Requirements

- [ ] Project description
- [ ] Steps to run `main.py`
- [ ] Names of all team members

---

## Suggested Team Workflow

- Agree on class and data contracts early.
- Complete Student 1 and Student 2 tasks first (foundation).
- Integrate Student 3 service logic after models and data loading are stable.
- Student 4 should finalize integration, tests, and documentation.
- Run tests before every merge.
