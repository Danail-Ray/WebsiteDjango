from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    twitter = models.OneToOneField(User, on_delete=models.CASCADE, related_name='twitter')
    pinterest = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pinterest')
    instagram = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instagram')
    bio = models.TextField(User)

    def __str__(self):
        return self.user.username


