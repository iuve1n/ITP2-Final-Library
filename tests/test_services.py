import unittest

from models.book import Book
from models.user import User
from services.library_service import borrow_book, return_book, yield_available_books


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

    def test_return_book_updates_history(self):
        borrow_book(10, 1, self.users, self.books)
        result = return_book(10, 1, self.users, self.books)

        self.assertTrue(result)
        self.assertTrue(self.books[1].get_availability())
        self.assertNotIn(1, self.users[10].active_borrowed_books)
        self.assertEqual(len(self.users[10].borrow_history), 1)
        self.assertEqual(self.users[10].borrow_history[0][0], 1)

    def test_yield_available_books_returns_available_only(self):
        self.books[2] = Book({"book_id": 2, "title": "Borrowed", "author": "Author", "available": False})

        available_books = list(yield_available_books(self.books))

        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].book_id, 1)


if __name__ == '__main__':
    unittest.main()
