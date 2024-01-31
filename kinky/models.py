from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


def user_image_upload_path(instance, filename):
    # instance.user is assumed to be a OneToOneField related to the User model
    return f"{instance.user.username}/images/{filename}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    bio = models.TextField(default="A bio has not been set yet...", blank=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='')
    image_counter = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to=user_image_upload_path,default='', blank=True, null=True, )

    def __str__(self):
        return self.user.username


class ImagesFromUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=user_image_upload_path, default='', blank=True, null=True, )

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return self.follower.username + ' follows ' + self.following.username
