import unittest
from transaction import Transaction
from book import Book
from member import Member

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        book = Book("Title", "Author", "ISBN123", 10, 2.0)
        member = Member("John Doe", "M001")
        transaction = Transaction(book, member)
        
        self.assertEqual(transaction.book, book)
        self.assertEqual(transaction.member, member)
        self.assertIsNotNone(transaction.issue_date)
        self.assertIsNotNone(transaction.due_date)
        self.assertIsNone(transaction.return_date)

if __name__ == '__main__':
    unittest.main()
