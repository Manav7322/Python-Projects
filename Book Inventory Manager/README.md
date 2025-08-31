
# 📚 Book Inventory Management System (SQLite + SQLAlchemy)

A simple command-line Book Inventory Management System built using **Python**, **SQLite**, and **SQLAlchemy ORM**.

This project demonstrates basic **CRUD operations** (Create, Read, Update, Delete) using SQLAlchemy with SQLite as the database backend.

---

## 🚀 Features
- Add new books with title, author, and year.
- View all books stored in the inventory.
- Update book details (title, author, year).
- Delete books from the inventory.
- Simple menu-driven command-line interface.

---

## 🛠️ Technologies Used
- **Python 3**
- **SQLite** (lightweight relational database)
- **SQLAlchemy ORM** (Object Relational Mapper)

---

## 📂 Project Structure
```
book_inventory/
│-- SqlAlchemy_setup.py   # Main script with database models and functions
│-- books_inventory.db    # SQLite database file (auto-created after running)
│-- README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository (or copy the script)**  
   ```bash
   git clone https://github.com/Manav7322/Python-Projects
   cd Book Inventory Manager
   ```

2. **Install dependencies**  
   SQLAlchemy is required. Install it with:
   ```bash
   pip install sqlalchemy
   ```

3. **Run the program**  
   ```bash
   python Book Inventory Manager.py
   ```

4. **Follow the menu options** to manage your book inventory.

---

## 📖 Example Usage

```
--- Book Inventory ---
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Exit

Enter choice: 1
Title: Python 101
Author: Guido
Year: 2023
```

```
--- Book Inventory ---
Enter choice: 2
<Book(id=1, title='Python 101', author='Guido', year=2023)>
```

---

## 🧑‍💻 Author
- Created by **Manav Gupta** while learning SQLAlchemy ORM basics 🚀

---

## ✅ Future Improvements
- Add search functionality (by title/author).
- Add user authentication system.
- Support for multiple tables (e.g., Users, Borrowed Books).
- Export book data to CSV/Excel.
