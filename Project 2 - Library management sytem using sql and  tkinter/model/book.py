from database.db_connection import db_connection
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def add_book(self):
        """Add a new book to the database"""
        query = """
        INSERT INTO books (title, author, isbn, total_copies, available_copies) 
        VALUES (%s, %s, %s, %s, %s)
        """
        return db_connection.execute_query(query, 
            (self.title, self.author, self.isbn, 
             self.total_copies, self.available_copies)
        )

    @classmethod
    def remove_book(cls, book_id):
        """Remove a book from the database"""
        query = "DELETE FROM books WHERE book_id = %s"
        return db_connection.execute_query(query, (book_id,))

    @classmethod
    def borrow_book(cls, user_id, book_id):
        """Borrow a book"""
        # Check if book is available
        availability_query = """
        SELECT available_copies FROM books WHERE book_id = %s
        """
        available_copies = db_connection.execute_query(availability_query, (book_id,))[0][0]

        if available_copies <= 0:
            return False

        # Borrow book
        borrow_query = """
        WITH update_book AS (
            UPDATE books 
            SET available_copies = available_copies - 1 
            WHERE book_id = %s
        )
        INSERT INTO borrowings (user_id, book_id, due_date) 
        VALUES (%s, %s, %s)
        """
        due_date = datetime.now() + timedelta(days=14)
        
        return db_connection.execute_query(borrow_query, 
            (book_id, user_id, book_id, due_date)
        )

    @classmethod
    def return_book(cls, borrow_id):
        """Return a borrowed book"""
        return_query = """
        WITH update_borrowing AS (
            UPDATE borrowings 
            SET returned_date = CURRENT_TIMESTAMP, 
                status = 'RETURNED' 
            WHERE borrow_id = %s
        ),
        update_book AS (
            UPDATE books b
            SET available_copies = available_copies + 1
            FROM borrowings br
            WHERE br.book_id = b.book_id AND br.borrow_id = %s
        )
        SELECT 1
        """
        return db_connection.execute_query(return_query, (borrow_id, borrow_id))

    @classmethod
    def search_books(cls, search_term):
        """Search for books by title or author"""
        query = """
        SELECT book_id, title, author, isbn, available_copies 
        FROM books 
        WHERE LOWER(title) LIKE %s OR LOWER(author) LIKE %s
        """
        search_pattern = f'%{search_term.lower()}%'
        return db_connection.execute_query(query, (search_pattern, search_pattern))