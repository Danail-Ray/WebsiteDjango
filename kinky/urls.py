from django.urls import path, include
from .views import signup
from .views import landing
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import profile



urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup', signup, name='signup'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('landing', landing, name='landing'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', profile, name='profile'),
]