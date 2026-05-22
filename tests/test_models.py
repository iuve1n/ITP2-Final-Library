import unittest
from models.book import Book
from models.person import Person
from models.user import User


class TestBook(unittest.TestCase):
    def test_availability_default_true(self):
        book = Book({"book_id": 1, "title": "Python", "author": "Baha", "available": True})
        self.assertTrue(book.get_availability())

    def test_set_availability_false(self):
        book = Book({"book_id": 1, "title": "Python", "author": "Baha", "available": True})
        book.set_availability(False)
        self.assertFalse(book.get_availability())

    def test_private_not_accessible(self):
        book = Book({"book_id": 1, "title": "Python", "author": "Baha", "available": True})
        with self.assertRaises(AttributeError):
            _ = book.__is_available

    def test_to_dict_format(self):
        book = Book({"book_id": 1, "title": "Python", "author": "Baha", "available": True})
        book_dict = book.to_dict()
        self.assertEqual(book_dict["author"], "Baha")
        self.assertEqual(book_dict["title"], "Python")


class TestPerson(unittest.TestCase):
    def test_person_role(self):
        person = Person({"user_id": 1, "name": "Bob"})
        self.assertEqual(person.get_role(), "Person")


class TestUser(unittest.TestCase):
    def test_get_role(self):
        user = User({"user_id": 1, "name": "Alice", "borrowed_books_list": None})
        self.assertEqual(user.get_role(), "Library User")

    def test_inherits_from_person(self):
        user = User({"user_id": 1, "name": "Alice", "borrowed_books_list": None})
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, "Alice")
        self.assertIsInstance(user, Person)

    def test_active_books_is_set(self):
        user = User({"user_id": 1, "name": "Alice", "borrowed_books_list": [5, 5, 5]})
        self.assertEqual(len(user.active_borrowed_books), 1)

    def test_add_book(self):
        user = User({"user_id": 1, "name": "Alice", "borrowed_books_list": None})
        user.add_book(10)
        self.assertIn(10, user.active_borrowed_books)

    def test_remove_book(self):
        user = User({"user_id": 1, "name": "Alice", "borrowed_books_list": None})
        user.add_book(10)
        user.remove_book(10)
        self.assertNotIn(10, user.active_borrowed_books)


if __name__ == "__main__":
    unittest.main()