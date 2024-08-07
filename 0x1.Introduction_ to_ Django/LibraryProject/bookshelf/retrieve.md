**Retrieve the book created**
from bookshelf.model import Book

book = Book.object.get(title="1984")
print(book.title,book.autjor,book.publish_year)

Expected output: 1984 George Orwell 1949


