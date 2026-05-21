from models.person import Person


class User(Person):
    def __init__(self, user_data):
        super().__init__(user_data)
        borrowed_books = user_data.get("borrowed_books_list") or []
        self.active_borrowed_books = set(borrowed_books)
        self.borrow_history = list(user_data.get("borrow_history", []))

    def get_role(self):
        return "Library User"

    def add_book(self, book_id):
        self.active_borrowed_books.add(book_id)

    def remove_book(self, book_id):
        self.active_borrowed_books.discard(book_id)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "borrowed_books_list": list(self.active_borrowed_books),
        }
