class User:
    def __init__(self,user_id,name,borrowed_books_list=None):
        self.user_id=int(user_id)
        self.name=name
        if borrowed_books_list==None:
            self.acive_borrowed_books=set()
        else:
            self.active_borrowed_books=set(borrowed_books_list)
        self.borrow_history=[]
    def get_role(self):
        return "Library User"
    
    def add_book(self,book_id):
        self.acive_borrowed_books.add(book_id)
    def remove_book(self,book_id):
        self.acive_borrowed_books.discard(book_id)