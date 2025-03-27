import hashlib
from database.db_connection import db_connection

class User:
    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = self._hash_password(password)
        self.is_admin = is_admin

    def _hash_password(self, password):
        """Hash the password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        """Register a new user"""
        query = """
        INSERT INTO users (username, password, email, is_admin) 
        VALUES (%s, %s, %s, %s)
        """
        return db_connection.execute_query(query, 
            (self.username, self.password, self.email, self.is_admin)
        )

    @classmethod
    def login(cls, username, password):
        """Authenticate user"""
        # Hash the input password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        query = """
        SELECT user_id, username, email, is_admin 
        FROM users 
        WHERE username = %s AND password = %s
        """
        result = db_connection.execute_query(query, (username, hashed_password))
        
        return result[0] if result else None

    @classmethod
    def get_borrowed_books(cls, user_id):
        """Retrieve books borrowed by a user"""
        query = """
        SELECT b.title, b.author, br.borrowed_date, br.due_date 
        FROM borrowings br
        JOIN books b ON br.book_id = b.book_id
        WHERE br.user_id = %s AND br.status = 'BORROWED'
        """
        return db_connection.execute_query(query, (user_id,))
