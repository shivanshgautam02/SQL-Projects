import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        try:
            # Create a connection pool
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 20,
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_NAME', 'library_management'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'password')
            )
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def get_connection(self):
        """Get a connection from the pool"""
        return self.connection_pool.getconn()

    def release_connection(self, connection):
        """Release the connection back to the pool"""
        self.connection_pool.putconn(connection)

    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        connection = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
           
            if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                connection.commit()
            
           
            if query.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            
            return None
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)
            if connection:
                connection.rollback()
            return None
        finally:
            if connection:
                cursor.close()
                self.release_connection(connection)

db_connection = DatabaseConnection()
