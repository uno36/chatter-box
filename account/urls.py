from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm
from .views import SignUpView, logout_view

app_name = 'account'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]
