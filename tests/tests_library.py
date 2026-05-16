import unittest
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.books = []

    def test_add_book(self):
        book = Book("Ai men Aisha", "Sh.Murtaza", "1968")
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)

    def test_delete_book(self):
        book = Book("Ai men Aisha", "Sh.Murtaza", "1968")
        self.library.add_book(book)
        self.library.delete_book(0)
        self.assertEqual(len(self.library.books), 0)

    def test_borrow_book(self):
        book = Book("Ai men Aisha", "Sh.Murtaza", "1968")
        self.library.add_book(book)
        self.library.borrow_book(0)
        self.assertEqual(self.library.books[0].status, "Borrowed")

    def test_return_book(self):
        book = Book("Ai men Aisha", "Sh.Murtaza", "1968", "Borrowed")
        self.library.add_book(book)
        self.library.return_book(0)
        self.assertEqual(self.library.books[0].status, "Available")

if __name__ == "__main__":
    unittest.main()