import unittest
from library import Library
from book import Book
from member import Member

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("Title", "Author", "ISBN123", 10, 2.0)
        library.add_book(book)
        self.assertEqual(len(library.books), 1)

    # Add more test cases for other methods...

if __name__ == '__main__':
    unittest.main()
