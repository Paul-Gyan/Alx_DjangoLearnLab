**Update the title of the created book**
from bookshelf.model import Book

book = Book.object.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
