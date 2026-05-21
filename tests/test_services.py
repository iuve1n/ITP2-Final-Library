import unittest

from models.book import Book
from models.user import User
from services.library_service import borrow_book


class TestServices(unittest.TestCase):
    def setUp(self):
        self.books = {
            1: Book({"book_id": 1, "title": "Sample Book", "author": "Author", "available": True})
        }
        self.users = {
            10: User({"user_id": 10, "name": "Jane Doe", "borrowed_books_list": []})
        }

    def test_borrow_book_success(self):
        result = borrow_book(10, 1, self.users, self.books)

        self.assertTrue(result)
        self.assertFalse(self.books[1].get_availability())
        self.assertIn(1, self.users[10].active_borrowed_books)

    def test_borrow_book_duplicate_raises(self):
        borrow_book(10, 1, self.users, self.books)
        with self.assertRaises(ValueError):
            borrow_book(10, 1, self.users, self.books)


if __name__ == '__main__':
    unittest.main()
