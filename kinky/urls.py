from django.urls import path, include
from .views import signup, delete_photo
from .views import landing
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import UserProfileView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import all_users
from .views import update_bio_view
from .views import upload_photo
from .views import follow_user
from .views import upload_profile
from .views import feed

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup', signup, name='signup'),
    path('landing', landing, name='landing'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>', UserProfileView.as_view(), name='profile'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('Users', all_users, name='Users'),
    path('changed-bio', update_bio_view, name='bio_update'),
    path('profile/<str:username>/upload_image', upload_photo, name='upload_image'),
    path('profile/<str:username>/follow_user', follow_user, name='follow_user'),
    path('upload_profile', upload_profile, name='upload_profile'),
    path('profile/<str:username>/delete_photo/<int:photo_id>', delete_photo, name='delete_photo'),
    path('feed', feed, name='feed'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
