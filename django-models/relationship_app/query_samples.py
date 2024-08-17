from django.db.models import Q

from .models import Author, Book, Library, Librarian

author = Author.objects.get(name='John Doe')
books_by_author = Book.objects.filter(author=author)
print(books_by_author)


# author_name = "George Orwell"
# author = Author.objects.get(name=author_name)
# books_by_author = Book.objects.filter(author=author)
# print('books by George Orwell:')
# for book in books_by_author:
#     print(book.title)


library = Library.objects.get(name='New York Public Library')
books_in_library = library.books.all()
print(books_in_library)





# library_name = "Wassa Library"
# library = Library.objects.get(name=library_name)
# books_in_library = library.bokks.all()
# print('books by Wassa Library:')
# for book in books_by_library:
#     print(book.title)

library = Library.objects.get(name='Wassa Library')
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for New York Public Library:")
print(librarian.name)






