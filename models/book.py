class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.__is_available = bool(available)
    def get_availability(self):
        return self.__is_available

    def set_availability(self, status):
        self.__is_available = bool(status)
        def __str__(self):
            status="Available" if self.__is_available else "Borrowed"
            return f"[{self.book_id}] '{self.title}' by {self.author}-{status}"