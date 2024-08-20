from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# admin_view.py


@user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
def admin_view(request):
    return render(request, 'admin_view.html')



