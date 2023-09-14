from datetime import datetime, timedelta

class Transaction:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=14)  # Assuming a 14-day borrowing period
        self.return_date = None
