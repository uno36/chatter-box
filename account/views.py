from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout

from .forms import AddUserForm



def logout_view(request):
    logout(request)
    return redirect('core:index')
