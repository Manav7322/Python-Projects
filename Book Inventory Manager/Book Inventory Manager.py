from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker

base = declarative_base()

engine = create_engine("sqlite:///books_inventory.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Book(base):
    __tablename__ = "books_inventory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})"


base.metadata.create_all(engine)


def add_book(title, author, year):
    new_book = Book(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()


def view_books():
    return session.query(Book).all()


def update_book(book_id, title, author, year):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.title = title
        book.author = author
        book.year = year
        session.commit()
    else:
        print("Book not found")


def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
    else:
        print("Book not found")


def menu():
    while True:
        print("\n--- Book Inventory ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            add_book(title, author, year)

        elif choice == "2":
            for row in view_books():
                print(row)

        elif choice == "3":
            book_id = int(input("Book ID: "))
            title = input("New Title: ")
            author = input("New Author: ")
            year = int(input("New Year: "))
            update_book(book_id, title, author, year)

        elif choice == "4":
            book_id = int(input("Book ID: "))
            delete_book(book_id)

        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
