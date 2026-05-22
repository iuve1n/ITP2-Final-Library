from datetime import datetime

from services.library_service import (
    borrow_book as service_borrow_book,
    get_books_by_author,
    get_user_history,
    return_book as service_return_book,
    yield_all_books,
    yield_all_users,
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


def format_user_line(user):
    borrowed_count = len(user.active_borrowed_books)
    return f"[{user.user_id}] {user.name} - Borrowed: {borrowed_count} book(s)"


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
        print("2. View All Books")
        print("3. View All Users")
        print("4. Find Books by Author")
        print("5. Borrow a Book")
        print("6. Return a Book")
        print("7. View User History")
        print("8. Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            available_books = list(yield_available_books(books))
            if not available_books:
                print("No available books at the moment.")
                continue
            for book in available_books:
                print(format_book_line(book))

        elif choice == "2":
            all_books = list(yield_all_books(books))
            if not all_books:
                print("No books in the library.")
                continue
            for book in all_books:
                print(format_book_line(book))

        elif choice == "3":
            all_users = list(yield_all_users(users))
            if not all_users:
                print("No users in the system.")
                continue
            for user in all_users:
                print(format_user_line(user))

        elif choice == "4":
            author_name = input("Enter author name: ").strip()
            books_by_author = get_books_by_author(author_name, books)
            if not books_by_author:
                print(f"No books found by author '{author_name}'.")
                continue
            print(f"Books by {author_name}:")
            for book in books_by_author:
                print(format_book_line(book))

        elif choice == "5":
            try:
                user_id = int(input("Enter user ID: ").strip())
                book_id = int(input("Enter book ID: ").strip())
                borrow_book_action(user_id, book_id, users, books)
                persist_library_state(books, users)
                print("Borrowed successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "6":
            try:
                user_id = int(input("Enter user ID: ").strip())
                book_id = int(input("Enter book ID: ").strip())
                return_book_action(user_id, book_id, users, books)
                persist_library_state(books, users)
                print("Returned successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "7":
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

        elif choice == "0":
            print("Exiting the library system.")
            break

        else:
            print("Invalid selection. Please choose a number from 1 to 8.")


if __name__ == "__main__":
    main()
