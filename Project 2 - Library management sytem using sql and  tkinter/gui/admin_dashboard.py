import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from models.book import Book

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")

       
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.book_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.book_frame, text="Book Management")
        self.create_book_management_tab()

        self.user_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.user_frame, text="User Management")
        self.create_user_management_tab()

    
        self.borrowing_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.borrowing_frame, text="Borrowing Records")
        self.create_borrowing_records_tab()

    def create_book_management_tab(self):
        # Add Book Section
        add_book_frame = tk.LabelFrame(self.book_frame, text="Add New Book")
        add_book_frame.pack(padx=10, pady=10, fill='x')

        # Title
        tk.Label(add_book_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(add_book_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # Author
        tk.Label(add_book_frame, text="Author:").grid(row=0, column=2, padx=5, pady=5)
        self.author_entry = tk.Entry(add_book_frame, width=30)
        self.author_entry.grid(row=0, column=3, padx=5, pady=5)

        # ISBN
        tk.Label(add_book_frame, text="ISBN:").grid(row=1, column=0, padx=5, pady=5)
        self.isbn_entry = tk.Entry(add_book_frame, width=30)
        self.isbn_entry.grid(row=1, column=1, padx=5, pady=5)

        # Total Copies
        tk.Label(add_book_frame, text="Total Copies:").grid(row=1, column=2, padx=5, pady=5)
        self.copies_entry = tk.Entry(add_book_frame, width=30)
        self.copies_entry.grid(row=1, column=3, padx=5, pady=5)

        # Add Book Button
        add_book_button = tk.Button(add_book_frame, text="Add Book", command=self.add_book)
        add_book_button.grid(row=2, column=0, columnspan=4, pady=10)

        # Book List
        self.book_tree = ttk.Treeview(self.book_frame, 
            columns=('Title', 'Author', 'ISBN', 'Total Copies', 'Available'), 
            show='headings'
        )
        self.book_tree.heading('Title', text='Title')
        self.book_tree.heading('Author', text='Author')
        self.book_tree.heading('ISBN', text='ISBN')
        self.book_tree.heading('Total Copies', text='Total Copies')
        self.book_tree.heading('Available', text='Available')
        self.book_tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Remove Book Button
        remove_book_button = tk.Button(self.book_frame, text="Remove Selected Book", command=self.remove_book)
        remove_book_button.pack(pady=10)

        # Load initial book list
        self.load_book_list()

    def create_user_management_tab(self):
        # User List
        self.user_tree = ttk.Treeview(self.user_frame, 
            columns=('Username', 'Email', 'Registered Date'), 
            show='headings'
        )
        self.user_tree.heading('Username', text='Username')
        self.user_tree.heading('Email', text='Email')
        self.user_tree.heading('Registered Date', text='Registered Date')
        self.user_tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Buttons for user management
        button_frame = tk.Frame(self.user_frame)
        button_frame.pack(pady=10)

        view_details_button = tk.Button(button_frame, text="View User Details", command=self.view_user_details)
        view_details_button.pack(side=tk.LEFT, padx=5)

        block_user_button = tk.Button(button_frame, text="Block User", command=self.block_user)
        block_user_button.pack(side=tk.LEFT, padx=5)

    def create_borrowing_records_tab(self):
        # Borrowing Records List
        self.borrowing_tree = ttk.Treeview(self.borrowing_frame, 
            columns=('User', 'Book', 'Borrowed Date', 'Due Date', 'Status'), 
            show='headings'
        )
        self.borrowing_tree.heading('User', text='User')
        self.borrowing_tree.heading('Book', text='Book')
        self.borrowing_tree.heading('Borrowed Date', text='Borrowed Date')
        self.borrowing_tree.heading('Due Date', text='Due Date')
        self.borrowing_tree.heading('Status', text='Status')
        self.borrowing_tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Refresh Button
        refresh_button = tk.Button(self.borrowing_frame, text="Refresh Records", command=self.load_borrowing_records)
        refresh_button.pack(pady=10)

    def add_book(self):
        # Validate inputs
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        
        try:
            total_copies = int(self.copies_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Total copies must be a number")
            return

        if not all([title, author, isbn]):
            messagebox.showerror("Error", "All fields are required")
            return

        # Create and add book
        book = Book(title, author, isbn, total_copies)
        book.add_book()

        # Clear entries and refresh list
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)

        # Refresh book list
        self.load_book_list()
        messagebox.showinfo("Success", "Book added successfully")

    def remove_book(self):
        # Get selected book
        selected_item = self.book_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a book to remove")
            return

        # Confirm removal
        if messagebox.askyesno("Confirm", "Are you sure you want to remove this book?"):
            # Get book details
            book_details = self.book_tree.item(selected_item)['values']
            
            # Remove book (use book_id if available)
            Book.remove_book(book_id=book_details[2])  
            
            # Refresh list
            self.load_book_list()

    def load_book_list(self):
 
        for i in self.book_tree.get_children():
            self.book_tree.delete(i)

       
        books = Book.search_books('')  
        for book in books:
            self.book_tree.insert('', 'end', values=book[1:])

    def view_user_details(self):
       
        messagebox.showinfo("User Details", "User details view not implemented")

    def block_user(self):
      
        messagebox.showinfo("Block User", "User blocking not implemented")

    def load_borrowing_records(self):
       
        messagebox.showinfo("Borrowing Records", "Records loading not implemented")