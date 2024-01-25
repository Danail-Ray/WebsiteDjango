from django.urls import path, include
from .views import signup
from .views import landing
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import profile
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup', signup, name='signup'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('landing', landing, name='landing'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', profile, name='profile'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
]
