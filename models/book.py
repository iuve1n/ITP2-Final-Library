class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.__is_available = bool(available)