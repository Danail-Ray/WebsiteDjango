# Generated by Django 5.0.1 on 2024-01-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0009_userprofile_likes_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='{{user}} has not set a bio yet...', null=True),
        ),
    ]