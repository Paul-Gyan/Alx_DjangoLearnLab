from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def admin_view(request):
    return render(request, 'admin_view.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'


admin_view = user_passes_test(is_admin)(admin_view)
librarian_view = user_passes_test(is_librarian)(librarian_view)
member_view = user_passes_test(is_member)(member_view)

