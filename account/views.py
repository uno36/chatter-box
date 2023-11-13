from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout

from .forms import AddUserForm


class SignUpView(View):
    template_name = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        form = AddUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('core:index')  # Change 'home' to 'login'
        return render(request, self.template_name, {'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('core:index')
