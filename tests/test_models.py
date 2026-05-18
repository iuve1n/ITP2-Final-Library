import unittest
from models.book import Book
from models.user import User
class TestBook(unittest.TestCase):
    def test_availability_default_true(self):
        book = Book (1,"Python","Baha",True)
        self.assertTrue(book.get_availability())
    
    def test_set_availability_false(self):
        book = Book (1,"Python","Baha",True)
        book.set_availability(False)
        self.assertFalse(book.get_availability())
    
    def test_private_not_accessible(self):
        book = Book (1,"Python","Baha",True)
        with self.assertRaises(AttributeError):
            _= book.__is_available
            
class TestUser(unittest.TestCase):
    def test_get_role(self):
        user=User(1,"Alice")
        self.assertEqual(user.get_role(),"Library User")
        
    def test_active_books_is_set(self):
        user=User(1,"Alice",[5,5,5])
        self.assertEqual(len(user.active_borrowed_books),1)
    
    def test_add_book(self):
        user=User(1,"Alice")
        user.add_book(10)
        self.assertIn(10,user.active_borrowed_books)
        
    def test_remove_book(self):
        user=User(1,"Alice")
        user.add_book(10)
        user.remove_book(10)
        self.assertNotIn(10,user.active_borrowed_books)
if __name__=="__main__":
    unittest.main()