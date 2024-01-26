from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    kinky_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    followers_count = models.IntegerField(default=0)
    bio = models.TextField(default=0, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='')

    def __str__(self):
        return self.kinky_user
