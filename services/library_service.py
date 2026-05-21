from datetime import datetime


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
