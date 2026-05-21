class User:
    def __init__(self,dict):
        self.user_id=int(dict["user_id"])
        self.name=dict["name"]
        if dict["borrowed_books_list"]==None:
            self.active_borrowed_books=set()
        else:
            self.active_borrowed_books=set(dict["borrowed_books_list"])
        self.borrow_history=[]
    def get_role(self):
        return "Library User"
    
    def get_id(self):
        return self.user_id
    
    def add_book(self,book_id):
        self.active_borrowed_books.add(book_id)
    def remove_book(self,book_id):
        self.active_borrowed_books.discard(book_id)