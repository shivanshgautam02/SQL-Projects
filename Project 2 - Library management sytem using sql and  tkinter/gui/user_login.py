import tkinter as tk
from tkinter import messagebox
from models.user import User

class LoginWindow:
    def __init__(self, root, on_login_callback):
        self.root = root
        self.on_login_callback = on_login_callback

        # Main login frame
        self.login_frame = tk.Frame(root, padx=50, pady=50)
        self.login_frame.pack(expand=True)

        # Title
        tk.Label(self.login_frame, text="Library Management System", 
                 font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

        # Username
        tk.Label(self.login_frame, text="Username:").grid(row=1, column=0, sticky='e', pady=5)
        self.username_entry = tk.Entry(self.login_frame, width=30)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Password
        tk.Label(self.login_frame, text="Password:").grid(row=2, column=0, sticky='e', pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*", width=30)
        self.password_entry.grid(row=2, column=1, pady=5)

        # Login Button
        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Register Button
        register_button = tk.Button(self.login_frame, text="Register", command=self.open_register_window)
        register_button.grid(row=4, column=0, columnspan=2, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate input
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        # Attempt login
        user = User.login(username, password)
        if user:
            
            self.on_login_callback(username, user[3])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_register_window(self):
        # Create registration window
        register_window = tk.Toplevel(self.root)
        register_window.title("Register New User")
        register_window.geometry("400x300")

        # Username
        tk.Label(register_window, text="Username:").pack(pady=5)
        username_entry = tk.Entry(register_window, width=30)
        username_entry.pack(pady=5)

        # Email
        tk.Label(register_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(register_window, width=30)
        email_entry.pack(pady=5)

        # Password
        tk.Label(register_window, text="Password:").pack(pady=5)
        password_entry = tk.Entry(register_window, show="*", width=30)
        password_entry.pack(pady=5)

        # Confirm Password
        tk.Label(register_window, text="Confirm Password:").pack(pady=5)
        confirm_password_entry = tk.Entry(register_window, show="*", width=30)
        confirm_password_entry.pack(pady=5)

        def register():
            # Get entry values
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            # Validate inputs
            if not username or not email or not password:
                messagebox.showerror("Error", "All fields are required")
                return

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                return

            # Create user
            try:
                user = User(username, email, password)
                user.register()
                messagebox.showinfo("Success", "User registered successfully")
                register_window.destroy()
            except Exception as e:
                messagebox.showerror("Registration Error", str(e))

        # Register Button
        register_button = tk.Button(register_window, text="Register", command=register)
        register_button.pack(pady=10)
