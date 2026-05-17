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

if __name__=="__main__":
    unittest.main()