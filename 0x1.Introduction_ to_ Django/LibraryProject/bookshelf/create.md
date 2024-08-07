**Create a book instance**
from bookshelf.model import Book

book = Book.object.create(title="1984",auhtor="George Orwell",publication_year=1949)

book.save()

Expected output: Book instance created successfully
