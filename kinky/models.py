from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You can customize this further

    # Your custom fields, if any

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    twitter = models.OneToOneField(User, on_delete=models.CASCADE, related_name='twitter')
    pinterest = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pinterest')
    instagram = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instagram')

    def __str__(self):
        return self.user.username


