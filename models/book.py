class Book:
    books_by_author = {}
    def __init__(self, book_data):
        self.book_id = int(book_data["book_id"])
        self.title = str(book_data["title"])
        self.author = str(book_data["author"])
        self.__is_available = bool(book_data.get("available", True))
        
        if self.author.lower() in Book.books_by_author:
            Book.books_by_author[self.author.lower()].append(self)
        else : 
            Book.books_by_author[self.author.lower()] = [self]
            

    def get_availability(self):
        return self.__is_available

    def get_id(self):
        return self.book_id

    def set_availability(self, status):
        self.__is_available = bool(status)

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.__is_available,
        }

    def __str__(self):
        status = "Available" if self.__is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"
