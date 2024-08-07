**Create a book instance**
from bookshelf.model import Book

book = Book(title="1984",auhtor="George Orwel",publication_year=1949)
book.object.create
book.save()

Expected output: Book instance created successfully
