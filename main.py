import requests
from library import Library
from book import Book
from member import Member
from datetime import datetime

def import_books_from_api(title=None, authors=None, isbn=None, publisher=None, num_books=20):
    base_url = "https://frappe.io/api/method/frappe-library"
    params = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "publisher": publisher,
        "num_books": num_books,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        books_data = response.json().get("message")
        return books_data
    else:
        print("Failed to fetch books from the API")
        return []

def main():
    # Create a library instance
    library = Library()

    # Import books from the Frappe API and create book records
    books_to_import = import_books_from_api(title="Harry Potter", num_books=30)
    
    for book_data in books_to_import:
        # Extract book details from the API response
        title = book_data.get("title")
        authors = book_data.get("authors")
        isbn = book_data.get("isbn")
        publisher = book_data.get("publisher")

        # Create a Book instance and add it to the library
        book = Book(title, authors, isbn, 0, 0.0)  # Initialize stock and rent fee to 0
        library.add_book(book)
    
    # Add members to the library
    member1 = Member("John Doe", "M001")
    member2 = Member("Jane Smith", "M002")
    library.add_member(member1)
    library.add_member(member2)

    # Issue books to members
    library.issue_book(library.books[0], member1)
    library.issue_book(library.books[1], member2)

    # Simulate book returns
    library.return_book(library.books[0], member1)
    library.return_book(library.books[1], member2)

    # Display member outstanding debts
    print(f"{member1.name}'s outstanding debt: Rs. {member1.outstanding_debt}")
    print(f"{member2.name}'s outstanding debt: Rs. {member2.outstanding_debt}")

if __name__ == "__main__":
    main()
