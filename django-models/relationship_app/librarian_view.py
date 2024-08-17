from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
def librarian_view(request):
    return render(request, 'librarian_view.html')

