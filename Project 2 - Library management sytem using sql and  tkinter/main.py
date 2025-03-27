import tkinter as tk
from gui.user_login import LoginWindow
from gui.admin_dashboard import AdminDashboard
from gui.user_dashboard import UserDashboard
from models.user import User

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        # Create login window
        self.login_window = LoginWindow(root, self.on_login)

    def on_login(self, username, is_admin):
        # Clear login window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Open appropriate dashboard based on user type
        if is_admin:
            AdminDashboard(self.root)
        else:
            UserDashboard(self.root)

def main():
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()