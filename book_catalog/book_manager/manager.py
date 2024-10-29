from .models import Book
from .database import get_engine, get_session

class BookManager:
    def __init__(self, db_url='sqlite:///:memory:'):
        self.engine = get_engine(db_url)
        self.session = get_session(self.engine)

    def add_book(self, title, author, year):
        if not title or not author or not isinstance(year, int) or year < 0:
            raise ValueError("Invalid book data")
        new_book = Book(title=title, author=author, year=year)
        self.session.add(new_book)
        self.session.commit()

    def get_all_books(self):
        return self.session.query(Book).all()

    def find_book(self, query):
        return self.session.query(Book).filter(
            (Book.title.contains(query)) | (Book.author.contains(query))
        ).all()

    def delete_book(self, book_id):
        book = self.session.query(Book).get(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
        else:
            raise ValueError(f"Book with id {book_id} does not exist")

    def update_book(self, book_id, title=None, author=None, year=None):
        book = self.session.query(Book).get(book_id)
        if not book:
            raise ValueError(f"Book with id {book_id} does not exist")

        if title:
            book.title = title
        if author:
            book.author = author
        if year is not None:
            if not isinstance(year, int) or year < 0:
                raise ValueError("Invalid year")
            book.year = year
        self.session.commit()