import tkinter as tk
from tkinter import ttk, messagebox
from models.book import Book
from models.user import User

class UserDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("User Dashboard")

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Search Books Tab
        self.search_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.search_frame, text="Search Books")
        self.create_search_tab()

        # My Books Tab
        self.my_books_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.my_books_frame, text="My Books")
        self.create_my_books_tab()

    def create_search_tab(self):
        # Search input
        search_label = tk.Label(self.search_frame, text="Search Books:")
        search_label.pack(pady=5)
        
        self.search_entry = tk.Entry(self.search_frame, width=50)
        self.search_entry.pack(pady=5)
        
        search_button = tk.Button(self.search_frame, text="Search", command=self.search_books)
        search_button.pack(pady=5)

        # Results Treeview
        self.book_tree = ttk.Treeview(self.search_frame, 
            columns=('Title', 'Author', 'ISBN', 'Available'), 
            show='headings'
        )
        self.book_tree.heading('Title', text='Title')
        self.book_tree.heading('Author', text='Author')
        self.book_tree.heading('ISBN', text='ISBN')
        self.book_tree.heading('Available', text='Available Copies')
        self.book_tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Borrow Button
        borrow_button = tk.Button(self.search_frame, text="Borrow Book", command=self.borrow_book)
        borrow_button.pack(pady=5)

    def create_my_books_tab(self):
        # Treeview for borrowed books
        self.borrowed_tree = ttk.Treeview(self.my_books_frame, 
            columns=('Title', 'Author', 'Borrowed Date', 'Due Date'), 
            show='headings'
        )
        self.borrowed_tree.heading('Title', text='Title')
        self.borrowed_tree.heading('Author', text='Author')
        self.borrowed_tree.heading('Borrowed Date', text='Borrowed Date')
        self.borrowed_tree.heading('Due Date', text='Due Date')
        self.borrowed_tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Refresh and Return Buttons
        button_frame = tk.Frame(self.my_books_frame)
        button_frame.pack(pady=5)

        refresh_button = tk.Button(button_frame, text="Refresh", command=self.load_borrowed_books)
        refresh_button.pack(side=tk.LEFT, padx=5)

        return_button = tk.Button(button_frame, text="Return Book", command=self.return_book)
        return_button.pack(side=tk.LEFT, padx=5)

        # Initial load of borrowed books
        self.load_borrowed_books()

    def search_books(self):
        # Clear previous results
        for i in self.book_tree.get_children():
            self.book_tree.delete(i)

        # Search books
        search_term = self.search_entry.get()
        if not search_term:
            messagebox.showwarning("Warning", "Please enter a search term")
            return

        results = Book.search_books(search_term)
        for book in results:
            self.book_tree.insert('', 'end', values=book[1:])

    def borrow_book(self):
        # Get selected book
        selected_item = self.book_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a book to borrow")
            return

        # Extract book details
        book_details = self.book_tree.item(selected_item)['values']
        
        # Confirm borrow
        if messagebox.askyesno("Confirm", f"Do you want to borrow '{book_details[0]}'?"):
            
            messagebox.showinfo("Success", "Book borrowed successfully")

    def load_borrowed_books(self):
        
        for i in self.borrowed_tree.get_children():
            self.borrowed_tree.delete(i)

    
        borrowed_books = User.get_borrowed_books(user_id=1)
        
        for book in borrowed_books:
            self.borrowed_tree.insert('', 'end', values=book)

    def return_book(self):
        # Get selected book
        selected_item = self.borrowed_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a book to return")
            return

        if messagebox.askyesno("Confirm", "Do you want to return this book?"):
           
            messagebox.showinfo("Success", "Book returned successfully")