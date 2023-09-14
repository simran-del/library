import datetime
from transaction import Transaction
from datetime import datetime



class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)

    def remove_book(self, book):
        # Remove a book from the library
        self.books.remove(book)

    def add_member(self, member):
        # Add a member to the library
        self.members.append(member)

    def remove_member(self, member):
        # Remove a member from the library
        self.members.remove(member)

    def issue_book(self, book, member):
        # Issue a book to a member
        if book.stock > 0:
            book.stock -= 1
            transaction = Transaction (book, member)
            self.transactions.append(transaction)
        else:
            print("Sorry, the book is out of stock.")

    def return_book(self, book, member):
        # Return a book from a member
        for transaction in self.transactions:
            if transaction.book == book and transaction.member == member and transaction.return_date is None:
                transaction.return_date = datetime.now()
                # Calculate and charge rent fee if applicable
                if transaction.return_date > transaction.due_date:
                    overdue_days = (transaction.return_date - transaction.due_date).days
                    rent_fee = overdue_days * book.rent_fee
                    member.outstanding_debt += rent_fee
                return

        print("Transaction not found or book already returned.")

    def search_book(self, title, author):
        # Search for a book by title and author
        matching_books = [book for book in self.books if book.title == title and book.author == author]
        return matching_books

    def charge_rent_fee(self, transaction):
        # Charge a rent fee on book returns (handled in return_book method)
        pass
