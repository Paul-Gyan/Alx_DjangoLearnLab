from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# member_view.py
@user_passes_test(lambda u: u.groups.filter(name='Member').exists())
def member_view(request):
    return render(request, 'member_view.html')
    









