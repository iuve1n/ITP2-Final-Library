from datetime import datetime

from services.library_service import (
    borrow_book as service_borrow_book,
    get_user_history,
    return_book as service_return_book,
    yield_available_books,
)
from utils.files_handler import initialize_system, save_data


def log_transaction(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        print(f"Transaction occurred at {now.strftime('%I:%M %p')}")
        return func(*args, **kwargs)

    return wrapper


@log_transaction
def borrow_book_action(user_id, book_id, users_dict, books_dict):
    return service_borrow_book(user_id, book_id, users_dict, books_dict)


def return_book_action(user_id, book_id, users_dict, books_dict):
    return service_return_book(user_id, book_id, users_dict, books_dict)


def format_book_line(book):
    availability = "Available" if book.get_availability() else "Borrowed"
    return f"[{book.book_id}] {book.title} by {book.author} - {availability}"


def persist_library_state(books_dict, users_dict):
    save_data("data/books.json", books_dict)
    save_data("data/users.json", users_dict)


def main():
    books, users = initialize_system()

    if not books:
        print("No books loaded. The library is empty or data is unavailable.")
    if not users:
        print("No users loaded. User operations may be restricted.")

    while True:
        print("\nLibrary Menu")
        print("1. View Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View User History")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            available_books = list(yield_available_books(books))
            if not available_books:
                print("No available books at the moment.")
                continue
            for book in available_books:
                print(format_book_line(book))

        elif choice == "2":
            try:
                user_id = int(input("Enter user ID: ").strip())
                book_id = int(input("Enter book ID: ").strip())
                borrow_book_action(user_id, book_id, users, books)
                persist_library_state(books, users)
                print("Borrowed successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: ").strip())
                book_id = int(input("Enter book ID: ").strip())
                return_book_action(user_id, book_id, users, books)
                persist_library_state(books, users)
                print("Returned successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: ").strip())
                history = get_user_history(user_id, users)
                if not history:
                    print("No borrowing history found for this user.")
                    continue
                for record in history:
                    print(record)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "5":
            print("Exiting the library system.")
            break

        else:
            print("Invalid selection. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
