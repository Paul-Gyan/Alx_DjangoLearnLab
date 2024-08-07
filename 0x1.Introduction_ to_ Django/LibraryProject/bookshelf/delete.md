**Delete the instance of the book**

from bookshelf.model import Book
book = Book.object.get(title="Nineteen Eighty-Four)
book.delete()
print(Book.object.all())

Expected output[]
