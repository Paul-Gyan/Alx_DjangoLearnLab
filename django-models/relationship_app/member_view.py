from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
def member_view(request):
    return render(request, 'member_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

member_view = user_passes_test(is_member)(member_view)


