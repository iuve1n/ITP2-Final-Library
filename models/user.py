from models.person import Person
class User(Person):
    def __init__(self,dict):
        super().__init__(dict)
        if dict["borrowed_books_list"] is None:
            self.active_borrowed_books= set()
        else:
            self.active_borrowed_books= set(dict["borrowed_books_list"])
        self.borrow_history = []
        
    def get_role(self):
        return"Library User"
    def add_book(self,book_id):
        self.active_borrowed_books.add(book_id)
    def remove_book(self, book_id):
        self.active_borrowed_books.discard(book_id)