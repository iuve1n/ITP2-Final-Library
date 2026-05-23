from datetime import datetime
from models.book import Book

def borrow_book(user_id, book_id, users_dict, books_dict):
    if user_id not in users_dict:
        raise ValueError("User does not exist.")
    if book_id not in books_dict:
        raise ValueError("Book does not exist.")

    user = users_dict[user_id]
    book = books_dict[book_id]

    if not book.get_availability():
        raise ValueError("Book is not available.")
    if book_id in user.active_borrowed_books:
        raise ValueError("Book already borrowed by user.")

    book.set_availability(False)
    user.add_book(book_id)
    return True


def return_book(user_id, book_id, users_dict, books_dict):
    if user_id not in users_dict:
        raise ValueError("User does not exist.")
    if book_id not in books_dict:
        raise ValueError("Book does not exist.")

    user = users_dict[user_id]
    book = books_dict[book_id]

    if book_id not in user.active_borrowed_books:
        raise ValueError("Book is not borrowed by this user.")

    user.remove_book(book_id)
    book.set_availability(True)
    user.borrow_history.append((book_id, datetime.now()))
    return True


def yield_available_books(books_dict):
    for book in books_dict.values():
        if book.get_availability():
            yield book


def yield_all_books(books_dict):
    for book in books_dict.values():
        yield book


def yield_all_users(users_dict):
    for user in users_dict.values():
        yield user


def get_books_by_author(author_name):
    author_name = author_name.lower()
    if author_name not in Book.books_by_author:
        raise ValueError("Author doesn't exist")
    return Book.books_by_author[author_name]


def get_user_history(user_id, users_dict):
    if user_id not in users_dict:
        raise ValueError("User does not exist.")
    return users_dict[user_id].borrow_history
