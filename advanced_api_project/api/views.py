from django.shortcuts import render
from rest_framework import generics
from .models import Book    
from .serializers import BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class BookListView(generics.ListCreateAPIView):
    """
    Retrieve a list of Books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    odering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a single Book ID
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete an existing Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
BookListView
This view provides a list of books a =nd allow users to filter, search, and order the list of books.

Filtering:
You can filter by Books by title, author, and publication year by adding query parametres to the URL. For example http://localhost:8000/api/books/?title=book_title

Searching:
You can search books by title and author by adding a search query parameter to the URL. For example:
http://localhost:8000/api/books/?search=book_author

Ordering:
You can order books by title and publication year by adding an ordering query parameter to the URL. For example:
http://localhost:8000/api/books/?ordering=publication_year
"""