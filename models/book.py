class Book:
    def __init__(self, dict, available=True):
        self.book_id = dict["book_id"]
        self.title = dict["title"]
        self.author = dict["author"]
        self.__is_available = bool(dict["available"])
    def get_availability(self):
        return self.__is_available
    
    def get_id(self):
        return self.book_id

    def set_availability(self, status):
        self.__is_available = bool(status)
    def __str__(self):
        status="Available" if self.__is_available else "Borrowed"
        return f"[{self.book_id}] '{self.title}' by {self.author}-{status}"