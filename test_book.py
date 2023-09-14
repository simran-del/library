import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Title", "Author", "ISBN123", 10, 2.0)
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.isbn, "ISBN123")
        self.assertEqual(book.stock, 10)
        self.assertEqual(book.rent_fee, 2.0)

if __name__ == '__main__':
    unittest.main()
