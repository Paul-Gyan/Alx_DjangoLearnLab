from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# librarian_view.py

@user_passes_test(lambda u: u.groups.filter(name='Librarian').exists())
def librarian_view(request):
    return render(request, 'librarian_view.html')


