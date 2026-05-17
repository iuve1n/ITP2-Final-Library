class User:
    def __init__(self,user_id,name,borrowed_books_list=None):
        self.user_id=int(user_id)
        self.name=name
        if borrowed_books_list==None:
            self.acive_borrowed_books=set()
        else:
            self.active_borrowed_books=set(borrowed_books_list)
        self.borrow_history=[]