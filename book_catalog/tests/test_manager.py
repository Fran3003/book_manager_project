import pytest
from book_manager.manager import BookManager

@pytest.fixture
def book_manager():
    return BookManager()

def test_add_book(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    books = book_manager.get_all_books()
    assert len(books) == 1
    assert books[0].title == "1984"

def test_add_book_with_invalid_data(book_manager):
    with pytest.raises(ValueError):
        book_manager.add_book("", "George Orwell", 1949)

    with pytest.raises(ValueError):
        book_manager.add_book("1984", "George Orwell", -1949)

def test_find_book_by_title(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    result = book_manager.find_book("1984")
    assert len(result) == 1

def test_delete_book(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    book_list = book_manager.get_all_books()
    book_manager.delete_book(book_list[0].id)
    books = book_manager.get_all_books()
    assert len(books) == 0

def test_delete_non_existent_book(book_manager):
    with pytest.raises(ValueError):
        book_manager.delete_book(999)

def test_update_book(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    book_list = book_manager.get_all_books()
    book_manager.update_book(book_list[0].id, title="Animal Farm", year=1945)
    updated_book = book_manager.get_all_books()[0]
    assert updated_book.title == "Animal Farm"
    assert updated_book.year == 1945

def test_update_book_invalid_year(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    book_list = book_manager.get_all_books()
    with pytest.raises(ValueError):
        book_manager.update_book(book_list[0].id, year=-1945)