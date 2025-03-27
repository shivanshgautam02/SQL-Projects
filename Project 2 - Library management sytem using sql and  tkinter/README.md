# 📚 Library Management System

Welcome to the **Library Management System**, a **GUI-based** application built with **Python, PostgreSQL, and Tkinter**. This system allows users to **register, borrow, and return books**, while the admin can efficiently **manage books and user records**. 🚀

This project is part of the **SQL Projects** repository. You can find it under:
📂 **[Project 2 - Library Management System using SQL and Tkinter](https://github.com/shivanshgautam02/SQL-Projects/tree/main/Project%202%20-%20Library%20management%20sytem%20using%20sql%20and%20%20tkinter)**

🔗 **Main Repository:** [SQL Projects](https://github.com/shivanshgautam02/SQL-Projects)

---

## ✨ Features

### 🔹 **Admin Features**
✅ Secure admin login.  
✅ Add new books to the library.  
✅ Remove books from the library.  
✅ View all borrowed books and their due dates.  
✅ Manage user accounts and borrowed book records.  

### 🔹 **User Features**
✅ Register using email, phone number, and password.  
✅ Log in to borrow books.  
✅ Return borrowed books before the due date.  
✅ View currently borrowed books and their due dates.  

---

## 🛠️ Tech Stack
- 🎨 **Frontend**: Tkinter (GUI-based desktop application)  
- 🖥️ **Backend**: Python with PostgreSQL using `psycopg2`  
- 🗄️ **Database**: PostgreSQL  

---

## 📂 Project Structure
```
Library-Management-System/
│-- database/
│   │-- db_connection.py        # Handles PostgreSQL database connection
│-- models/
│   │-- book.py                 # Book-related operations
│   │-- user.py                 # User authentication and management
│-- gui/
│   │-- admin_dashboard.py      # Admin dashboard UI
│   │-- user_dashboard.py       # User dashboard UI
│   │-- user_login.py           # User login UI
│-- main.py                      # Main entry point of the system
│-- setup_database.sql           # SQL script to set up database tables
│-- requirements.txt             # Required Python dependencies
│-- README.md                    # Project documentation
```

---

## 🚀 Installation & Setup

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/shivanshgautam02/SQL-Projects.git
cd "SQL-Projects/Project 2 - Library management sytem using sql and  tkinter"
```

### **Step 2: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 3: Set Up the Database**
- Create a PostgreSQL database named `library_db`.
- Update database credentials in `database/db_connection.py`.
- Run the SQL script:
```sh
psql -U your_user -d library_db -f setup_database.sql
```

### **Step 4: Set Up Environment Variables**
Before running the application, set up the following **environment variables**:  
```sh
LOCALHOST=localhost
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

💡 Make sure to configure these in your **system environment variables** or a `.env` file for security.  

---

### **Step 5: Run the Application**
```sh
python main.py
```

🚀 Your Library Management System is now up and running!  

---

## 🔑 Admin Credentials
Use the following credentials to log in as an **admin**:  
📧 **Email**: `admin@mybook.com`  
🔑 **Password**: `admin123`  

🔐 You can modify these credentials in the database if needed.  

---

## 📜 License
This project is open-source under the **MIT License**. Feel free to contribute and improve the system!  

---


