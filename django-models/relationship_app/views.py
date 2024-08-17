from django.shortcuts import render
from .models import Book

def list_book(request):
    books = Book.objects.all()
    return render(request, 'templates\relationship_app\list_books.html', {'books': books})
    

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
