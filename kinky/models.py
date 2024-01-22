from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You can customize this further

    # Your custom fields, if any

    def __str__(self):
        return self.username

