-- Create Database
CREATE DATABASE library_management;


-- Create Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Books Table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    total_copies INTEGER NOT NULL,
    available_copies INTEGER NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Borrowing Table
CREATE TABLE borrowings (
    borrow_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    book_id INTEGER REFERENCES books(book_id),
    borrowed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP NOT NULL,
    returned_date TIMESTAMP,
    status VARCHAR(20) DEFAULT 'BORROWED' 
        CHECK (status IN ('BORROWED', 'RETURNED', 'OVERDUE'))
);

-- Create an admin user
INSERT INTO users (username, password, email, is_admin) 
VALUES ('admin', 'admin_password_hash', 'admin@library.com', TRUE);