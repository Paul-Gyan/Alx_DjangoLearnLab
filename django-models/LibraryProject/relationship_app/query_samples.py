from django.db.models import Q

from .models import Author, Book, Library, Librarian

author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print('books by George Orwell:')
for book in books_by_author:
    print(book.title)


library_name = "Wassa Library"
library = Library.objects.get(name=library_name)
books_by_library = Book.objects.filter(library=library)
print('books by Wassa Library:')
for book in books_by_library:
    print(book.title)

librarian = get_librarian_for_library(library_name)
print('Librarian for', library_name, ':', librarian)






