import unittest
from io import StringIO
from unittest.mock import patch

from models.book import Book
from models.user import User
import main


class TestLibraryMain(unittest.TestCase):
    def setUp(self):
        self.books = {
            1: Book({"book_id": 1, "title": "Sample Book", "author": "Author", "available": True})
        }
        self.users = {
            10: User({"user_id": 259929, "name": "Miras Tastan", "borrowed_books_list": []})
        }

    def test_borrow_book_action_success_prints_transaction_time(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            result = main.borrow_book_action(10, 1, self.users, self.books)

        self.assertTrue(result)
        self.assertFalse(self.books[1].get_availability())
        self.assertIn(1, self.users[10].active_borrowed_books)
        self.assertIn("Transaction occurred at", fake_out.getvalue())

    def test_borrow_book_action_duplicate_raises(self):
        main.borrow_book_action(10, 1, self.users, self.books)
        with self.assertRaises(ValueError):
            main.borrow_book_action(10, 1, self.users, self.books)


if __name__ == "__main__":
    unittest.main()
