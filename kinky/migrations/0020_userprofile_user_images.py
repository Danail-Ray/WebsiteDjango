# Generated by Django 5.0.1 on 2024-01-30 13:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0019_userprofile_image_counter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_images',
            field=models.ManyToManyField(blank=True, related_name='user_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
