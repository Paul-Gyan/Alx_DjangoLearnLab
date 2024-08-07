**Create a book instance**
from bookshelf.model import Book

book = Book(title="1984",auhtor="George Orwel",publication_year=1949)
book.object.create
book.save()

Expected output: Book instance created successfully

**Retrieve the book created**
from bookshelf.model import Book

book = Book.object.get(title="1984")
print(book.title,book.autjor,book.publish_year)

Expected output: 1984 George Orwell 1949

**Update the title of the created book**
from bookshelf.model import Book

book = Book.object.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

Expected output: Nineteen Eighty-Four

**Delete the instance of the book**

from bookshelf.model import Book
book = Book.object.get(title="Nineteen Eighty-Four)
book.delete()
print(Book.object.all())

Expected output[]



